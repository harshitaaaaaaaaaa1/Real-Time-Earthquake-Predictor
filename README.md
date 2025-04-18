

# Real-Time Earthquake Predictor 🌎⚡

## **Project Overview**

Countless dollars and entire scientific careers have been dedicated to predicting where and when the next big earthquake will strike. Unlike weather forecasting, which has significantly improved with satellites and advanced mathematical models, earthquake prediction has faced repeated failures due to the highly uncertain conditions inside the Earth.

Now, with the help of **Artificial Intelligence (AI)**, a growing number of scientists believe that analyzing massive amounts of seismic data can help better understand earthquake behavior, leading to quicker and more accurate **early warnings**.  

This project proposes a **simple yet powerful solution** — predicting or forecasting likely places that could experience an earthquake **in the next 7 days**.  

To make it **user-friendly**, a **web application** has been developed that:
- Extracts **live earthquake data** updated every minute by **USGS.gov**.
- **Predicts** the next likely place worldwide to get hit by an earthquake in **real-time**.
- Displays results with **Google Maps API** integration for better visualization.

This helps in **hazard assessments** for builders, real estate businesses, and infrastructure planning, while also aiming to **save lives** through early warnings.

---

## **Code Structure**

```bash
Data/    
  ├── ETL_USGS_EarthQuake.ipynb  # ETL and EDA Notebook
  ├── ETL_USGS_EarthQuake.html   # HTML version of ETL Notebook
  ├── Earthquake.db              # Cleaned Data (Database)
  └── Earthquake_data.db         # Backup Database

models/
  ├── Earthquake-prediction-ML-workflow.ipynb  # ML Pipeline and Modeling
  └── Earthquake-prediction-ML-workflow.html   # HTML version of ML Workflow

Webapp/
  └── main.py   # Flask Application: Data Extraction → Prediction → Google Maps Conversion
```

---

## **Recommended Walkthrough**
- **ETL Process:**  
  Open `Data/ETL_USGS_EarthQuake.ipynb` or `Data/ETL_USGS_EarthQuake.html`.
  
- **Machine Learning Workflow:**  
  Open `models/Earthquake-prediction-ML-workflow.ipynb` or `models/Earthquake-prediction-ML-workflow.html`.

---

## **Requirements**

| Package            | Version |
|--------------------|---------|
| click              | 7.1.2   |
| Flask              | 1.1.2   |
| gunicorn           | 20.0.4  |
| itsdangerous       | 1.1.0   |
| Jinja2             | 2.11.2  |
| joblib             | 0.16.0  |
| MarkupSafe         | 1.1.1   |
| numpy              | 1.19.1  |
| pandas             | 1.1.0   |
| python-dateutil    | 2.8.1   |
| pytz               | 2020.1  |
| scikit-learn       | 0.23.1  |
| scipy              | 1.5.2   |
| six                | 1.15.0  |
| sklearn            | 0.0     |
| SQLAlchemy         | 1.3.18  |
| threadpoolctl      | 2.1.0   |
| Werkzeug           | 1.0.1   |
| xgboost            | 1.1.1   |

> **Environment:**  
> Python 3.x  

---

## **Steps to Clone the Repository**

```bash
git clone https://github.com/harshitaaaaaaaaaa1/Real-Time-Earthquake-Predictor.git
cd Realtime-Earthquake-forecasting
```

---

## **Execution Steps**

1. **Open** Visual Studio Code (VS Code).
2. **Open Terminal** → Select **New Terminal**.
3. Create a **virtual environment**:
   ```bash
   python3 -m venv <your_environment_name>
   ```
   > (If an error occurs, make sure virtual environment tools are installed.)
4. **Activate the environment**:
   ```bash
   source <your_environment_name>/bin/activate
   ```
5. **Upgrade pip**:
   ```bash
   pip install --upgrade pip
   ```
6. **Install all required packages**:
   ```bash
   pip install -r requirements.txt
   ```
7. **Run the application**:
   ```bash
   python main.py
   ```
8. **Open your browser** and go to **localhost** once the application starts.

9. **Use the date slider** on the web app to choose dates for prediction.

---

> **Note:**  
> Always ensure that your virtual environment is active before running the app!

