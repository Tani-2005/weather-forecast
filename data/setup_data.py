import kagglehub
import shutil
import os

def initialize_project():
    # 1. Create the data directory if it doesn't exist
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created directory: {data_dir}")

    # 2. Download latest version from Kaggle
    print("Downloading dataset from Kaggle...")
    downloaded_path = kagglehub.dataset_download("nelgiriyewithana/global-weather-repository")

    # 3. Locate the CSV in the downloaded folder and move it to /data
    for file in os.listdir(downloaded_path):
        if file.endswith(".csv"):
            source_path = os.path.join(downloaded_path, file)
            destination_path = os.path.join(data_dir, "global_weather_repository.csv")
            
            # Move and rename the file
            shutil.copy(source_path, destination_path)
            print(f"Dataset successfully moved to: {destination_path}")
            break

if __name__ == "__main__":
    initialize_project()