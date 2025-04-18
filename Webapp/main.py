from flask import Flask, render_template, request
from datetime import datetime, timedelta
import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Global variables
earthquake_live = None
days_out_to_predict = 7

def prepare_earthquake_data_and_model(days_out_to_predict=7, max_depth=3, eta=0.1):
    """
    Prepares earthquake data and trains an XGBoost model.
    Returns: Pandas DataFrame with prediction results.
    """
    try:
        # Fetch the latest earthquake data from USGS
        df = pd.read_csv('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv')
        df = df.sort_values('time', ascending=True)
        df['date'] = df['time'].str[:10]

        # Keep necessary columns
        df = df[['date', 'latitude', 'longitude', 'depth', 'mag', 'place']]
        df['place'] = df['place'].str.split(', ').str[-1]  # Extract country/region

        # Calculate mean lat/lon for each place
        df_coords = df.groupby('place', as_index=False).mean()
        df = df[['date', 'depth', 'mag', 'place']]
        df = pd.merge(df, df_coords, on='place', how='inner')

        # Apply rolling averages for trends
        eq_data, df_live = [], []
        for place in df['place'].unique():
            temp_df = df[df['place'] == place].copy()
            temp_df['depth_avg_22'] = temp_df['depth'].rolling(22).mean()
            temp_df['mag_avg_22'] = temp_df['mag'].rolling(22).mean()
            temp_df['mag_outcome'] = temp_df['mag_avg_22'].shift(-days_out_to_predict)
            df_live.append(temp_df.tail(days_out_to_predict))
            eq_data.append(temp_df)

        df = pd.concat(eq_data).dropna()
        df['mag_outcome'] = (df['mag_outcome'] > 2.5).astype(int)
        df_live = pd.concat(df_live).dropna()

        # Train the XGBoost model
        features = ['depth_avg_22', 'mag_avg_22']
        X_train, X_test, y_train, y_test = train_test_split(df[features], df['mag_outcome'], test_size=0.3, random_state=42)

        dtrain = xgb.DMatrix(X_train, label=y_train)
        dtest = xgb.DMatrix(X_test, label=y_test)

        params = {
            'objective': 'binary:logistic',
            'booster': 'gbtree',
            'eval_metric': 'auc',
            'max_depth': max_depth,
            'eta': eta
        }

        xgb_model = xgb.train(params, dtrain, num_boost_round=1000)

        # Predict on live data
        dlive = xgb.DMatrix(df_live[features])
        preds = xgb_model.predict(dlive)

        # Add predictions
        df_live = df_live[['date', 'place', 'latitude', 'longitude']]
        df_live['preds'] = preds
        df_live = df_live.groupby(['date', 'place']).mean()
        df_live['date'] = pd.to_datetime(df_live['date']) + timedelta(days=days_out_to_predict)

        return df_live
    except Exception as e:
        print(f"Error preparing data: {e}")
        return pd.DataFrame()

def get_earthquake_estimates(desired_date, df_live):
    live_data = df_live[df_live['date'] == desired_date]
    locations = []
    for _, row in live_data.iterrows():
        if row['preds'] > 0.3:
            locations.append(f"new google.maps.LatLng({row['latitude']}, {row['longitude']})")
    return ",".join(locations)

@app.before_request
def startup():
    global earthquake_live
    earthquake_live = prepare_earthquake_data_and_model()

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        horizon_int = int(request.form.get('slider_date_horizon', 0))
        horizon_date = datetime.today() + timedelta(days=horizon_int)
        return render_template(
            'home.html',
            date_horizon=horizon_date.strftime('%m/%d/%Y'),
            earthquake_horizon=get_earthquake_estimates(horizon_date.strftime('%Y-%m-%d'), earthquake_live),
            current_value=horizon_int,
            days_out_to_predict=days_out_to_predict
        )
    return render_template(
        'home.html',
        date_horizon=datetime.today().strftime('%m/%d/%Y'),
        earthquake_horizon='',
        current_value=0,
        days_out_to_predict=days_out_to_predict
    )

@app.route("/index")
def index():
    return render_template('index.html', days_out_to_predict=days_out_to_predict)

@app.route("/predict_man", methods=['POST', 'GET'])
def predict_man():
    if request.method == 'GET':
        return render_template('predict_man.html', result=None, date_horizon=datetime.today().strftime('%m/%d/%Y'))
    try:
        horizon_int = int(request.form.get('slider_date_horizon', 0))
        horizon_date = datetime.today() + timedelta(days=horizon_int)
        prediction_probability = np.random.uniform(0, 1)

        prediction_category = "Low Chances" if prediction_probability < 0.3 else ("Moderate Chances" if prediction_probability < 0.6 else "High Chances")

        return render_template(
            'predict_man.html',
            result=prediction_category,
            latitude=request.form.get('latitude', 'N/A'),
            longitude=request.form.get('longitude', 'N/A'),
            depth=request.form.get('depth', 'N/A'),
            magnitude=request.form.get('magnitude', 'N/A'),
            date_horizon=horizon_date.strftime('%m/%d/%Y'),
            earthquake_horizon=get_earthquake_estimates(horizon_date.strftime('%Y-%m-%d'), earthquake_live),
            current_value=horizon_int,
            days_out_to_predict=days_out_to_predict
        )
    except Exception as e:
        return f"Error: {e}"
@app.route('/about')
def about_page():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
