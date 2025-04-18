Project Overview

Countless dollars and entire scientific careers have been dedicated to predicting where and when the next big earthquake will strike. But unlike weather forecasting, which has significantly improved with the use of better satellites and more powerful mathematical models, earthquake prediction has been marred by repeated failure due to highly uncertain conditions of earth and its surroundings. Now, with the help of artificial intelligence, a growing number of scientists say changes in the way they can analyze massive amounts of seismic data can help them better understand earthquakes, anticipate how they will behave, and provide quicker and more accurate early warnings. This helps in hazzard assessments for many builders and real estate business for infrastructure planning from business perspective. Also many lives can be saved through early warning. This project aims a simple solution to above problem by predicting or forecasting likely places to have earthquake in next 7 days. For user-friendly part, this project has a web application that extracts live data updated every minute by USGS.gov and predicts next likely place world wide to get hit by an earthquake, hence a realtime solution is provided.

Code files
Data/ : Notebook and HTML file ETL_USGS_EarthQuake.ipybn for ETL and EDA part of the project, and it also contains cleaned data in Earthquake.db & Earthquake_data.db format saved after ETL process

models/ : Notebook and HTML file Earthquake-prediction-ML-workflow.ipybn which has all the implementation after related to Prediction steps and Machine Learning pipeline.

Webapp/ : all the necessary routing python files in main.py for flask application i.e from data extraction to modeling application and convert prediction co-ordinates to google maps api format.

I have implemented all the neccesary steps in these IPYBN notebooks. I recommend for project walkthrough follow -

For ETL walkthrough open Data/ETL_USGS_EarthQuake.ipybn or Data/ETL_USGS_EarthQuake.html

Next, go to models/Earthquake-prediction-ML-workflow.ipybn or models/Earthquake-prediction-ML-workflow.html for ML and workflow.

Instructions to run the project
Requirements

click==7.1.2
Flask==1.1.2
gunicorn==20.0.4
itsdangerous==1.1.0
Jinja2==2.11.2
joblib==0.16.0
MarkupSafe==1.1.1
numpy==1.19.1
pandas==1.1.0
python-dateutil==2.8.1
pytz==2020.1
scikit-learn==0.23.1
scipy==1.5.2
six==1.15.0
sklearn==0.0
SQLAlchemy==1.3.18
threadpoolctl==2.1.0
Werkzeug==1.0.1
xgboost==1.1.1
python3.x
Linux/Mac Users

Note for windows user : install gitbash and proceed with same instruction as linux.

EXECUTION STEPS
1.Open VS Code
2.Click on Terminal and select new terminal
3. To create Virtual environment eneter ‘-m venv <<any environment name>>’ (If error occurs, download virtual environment for python)
4. <<any environment name>>/bin/activate
5. pip install --upgrade pip 
6.To install the packages ‘pip install -r requirements.txt’. Requeriments.txt file contains all the packages necessary for execution. 
7.Run application with ‘python main.py’ i.e in root directory of project repo.
8. Go to local host when application starts and use slider to choose dates for prediction in app.


