import kagglehub
import shutil
import os

def initialize_project():
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created directory: {data_dir}")
    print("Downloading dataset from Kaggle...")
    downloaded_path = kagglehub.dataset_download("nelgiriyewithana/global-weather-repository")
    for file in os.listdir(downloaded_path):
        if file.endswith(".csv"):
            source_path = os.path.join(downloaded_path, file)
            destination_path = os.path.join(data_dir, "global_weather_repository.csv")
            shutil.copy(source_path, destination_path)
            print(f"Dataset successfully moved to: {destination_path}")
            break

if __name__ == "__main__":
    initialize_project()
