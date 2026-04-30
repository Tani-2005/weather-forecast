import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def plot_spatial_weather(df):
    fig = px.scatter_geo(df, 
                         lat='latitude', 
                         lon='longitude', 
                         color='temperature_celsius',
                         hover_name='location_name',
                         title='Global Temperature Distribution',
                         color_continuous_scale='RdBu_r')
    fig.update_layout(geo=dict(showframe=False, showcoastlines=True))
    return fig

def plot_air_quality_correlation(df):
    aq_cols = [
        'air_quality_PM2.5', 
        'air_quality_Carbon_Monoxide', 
        'air_quality_Ozone', 
        'temperature_celsius', 
        'humidity'
    ]
    corr = df[aq_cols].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='RdBu_r', center=0, fmt=".2f")
    plt.title("Environmental Impact: Air Quality vs Weather")
    plt.tight_layout()
    return plt
