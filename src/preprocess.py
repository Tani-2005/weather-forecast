import pandas as pd
from sklearn.ensemble import IsolationForest

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    
    # Date conversion
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    
    # Anomaly Detection using Isolation Forest
    iso = IsolationForest(contamination=0.02, random_state=42)
    df['is_anomaly'] = iso.fit_predict(df[['temperature_celsius', 'precip_mm']])
    df['is_anomaly'] = df['is_anomaly'].apply(lambda x: 1 if x == -1 else 0)
    
    return df
