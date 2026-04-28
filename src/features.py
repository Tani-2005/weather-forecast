import pandas as pd

def engineer_weather_features(df):
    # Sort for time-series operations
    df = df.sort_values(['location_name', 'last_updated'])
    
    # Basic Requirement: Time Series Features
    df['temp_lag_1'] = df.groupby('location_name')['temperature_celsius'].shift(1)
    
    # Advanced Requirement: Environmental Interactions
    df['temp_humidity_index'] = df['temperature_celsius'] * (df['humidity'] / 100)
    
    # Drop rows where lag created NaNs
    return df.dropna(subset=['temp_lag_1'])