import os
import pandas as pd

DATA_PATH = "data/raw"

print("Current Working Directory:", os.getcwd())
print("Looking inside:", DATA_PATH)

csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

print("CSV Files Found:", csv_files)

for file in csv_files:
    path = os.path.join(DATA_PATH, file)

    print(f"\nReading: {file}")

    df = pd.read_csv(path)

    print("Shape:", df.shape)
    print(df.head())