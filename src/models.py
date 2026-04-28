import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from prophet import Prophet
import shap
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error

def train_xgboost_model(train_df, test_df, features):
    target = 'temperature_celsius'
    
    X_train, y_train = train_df[features], train_df[target]
    X_test, y_test = test_df[features], test_df[target]
    
    model = XGBRegressor(n_estimators=100, max_depth=5, learning_rate=0.1, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"XGBoost RMSE: {rmse:.2f}°C")
    
    return model, X_train

def generate_shap_explanation(model, X_train):
    """Generates Advanced Explainable AI visual."""
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_train)
    
    plt.figure(figsize=(10, 6))
    plt.title("Explainable AI: Feature Impact on Temperature Forecast")
    shap.summary_plot(shap_values, X_train, show=False)
    plt.tight_layout()
    return plt

def train_prophet_model(df, location="Kabul"):
    """Advanced Time Series Forecasting."""
    city_df = df[df['location_name'] == location].copy()
    
    prophet_df = pd.DataFrame({
        'ds': city_df['last_updated'],
        'y': city_df['temperature_celsius']
    })
    
    model = Prophet(interval_width=0.95, yearly_seasonality=True, daily_seasonality=False)
    model.fit(prophet_df)
    
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    
    return model, forecast

def plot_prophet_forecast(model, forecast, location_name):
    fig = model.plot(forecast)
    plt.title(f"30-Day Trend Forecast for {location_name} (Prophet)")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    return fig