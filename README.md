# Weather Trend Forecasting - PM Accelerator Tech Assessment

> **PM Accelerator Mission:** To help international professionals transition quickly into product management, secure top offers from top-tier companies, and become product leaders.

##  Project Overview
This repository contains an end-to-end data science pipeline designed to forecast global weather trends. Built for the PM Accelerator technical assessment, this project goes beyond basic exploratory analysis by implementing **Advanced Assessment** requirements, including Explainable AI (SHAP), Time-Series Forecasting (Prophet), and Automated Anomaly Detection.

The goal of this project is to showcase how raw, multi-dimensional weather data can be transformed into actionable, product-ready insights for decision-makers.

---

##  Advanced Techniques Implemented

* **Explainable AI (Feature Importance):** Instead of standard feature weighting, this pipeline uses **SHAP (SHapley Additive exPlanations)** to unpack the "black box" of the XGBoost model. It explains exactly *how* variables like humidity and wind speed drive temperature forecasts.
* **Time-Series Forecasting:** Integrated Facebook's **Prophet** library to handle daily seasonality, weekly trends, and long-term climate patterns for specific locations.
* **Automated Anomaly Detection:** Implemented an `IsolationForest` algorithm to automatically detect and flag extreme weather events (outliers) without relying on hard-coded thresholds.
* **Spatial & Environmental Impact Analysis:** Utilized `Plotly` to map global temperature distributions and analyzed the correlation between air quality metrics (PM2.5, Carbon Monoxide, Ozone) and weather conditions.

---

##  Repository Structure

The project follows a modular, production-ready architecture rather than a single monolithic notebook.

```text
weather-forecast-assessment/
├── data/
│   └── global_weather_repository.csv  # Auto-downloaded via setup_data.py
├── notebooks/
│   └── exploration_and_modeling.ipynb # The master notebook containing all EDA and models
├── src/                               # Modular Python source code
│   ├── __init__.py
│   ├── preprocess.py                  # Data cleaning & Isolation Forest anomaly detection
│   ├── features.py                    # Lag features, rolling averages, and indices
│   ├── models.py                      # XGBoost, SHAP explainability, and Prophet models
│   └── visualization.py               # Spatial mapping and Environmental correlation heatmaps
├── README.md                          # Project documentation
├── requirements.txt                   # Dependency list
└── setup_data.py                      # Automated Kaggle data ingestion script
```

## Setup and Installation
To run this project locally and reproduce the results, follow these steps:
1. Clone the repository:
```
git clone <your-github-repo-link>
cd weather-forecast-assessment
```
2. Install dependencies:
It is recommended to use a virtual environment.
```
pip install -r requirements.txt
```
3. Fetch the Dataset:
Run the setup script to automatically pull the latest dataset from Kaggle via API and place it in the /data directory.
```
python setup_data.py
```
4. Run the Analysis:
Launch Jupyter Notebook and open notebooks/exploration_and_modeling.ipynb.
```
jupyter notebook
```
Note: The master notebook is configured to automatically import and reload the custom modules from the src/ directory.

## Key Insights & Findings
- Anomaly Detection: The Isolation Forest successfully flagged ~2% of the dataset as extreme weather anomalies, preventing these outliers from skewing the standard forecast models.

- Environmental Correlations: The advanced EDA revealed distinct correlations between specific weather conditions (like humidity) and drops in air quality (PM2.5 and Ozone).

- Model Performance: By ensembling lagged features with XGBoost and capturing seasonal trends with Prophet, the pipeline provides a robust framework for short and long-term temperature forecasting.


## Demo Video
[Insert Link to your 1-2 minute YouTube/Drive Demo Video Here]

Developed for the PM Accelerator Internship Assessment.


***

### What to do next:
1. Paste this into your repository.
2. Replace `<your-github-repo-link>` under step 1 with your actual public GitHub URL.
3. Replace `[Insert Link to your 1-2 minute YouTube/Drive Demo Video Here]` at the bottom with the link to the video you record.

This README is highly polished and hits every single requirement they asked for. Are
