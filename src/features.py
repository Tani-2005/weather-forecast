import pandas as pd
def engineer_weather_features(df):
    df = df.sort_values(['location_name', 'last_updated']) # Sorts time-series operations
    df['temp_lag_1'] = df.groupby('location_name')['temperature_celsius'].shift(1) 
    df['temp_humidity_index'] = df['temperature_celsius'] * (df['humidity'] / 100)
    return df.dropna(subset=['temp_lag_1'])
