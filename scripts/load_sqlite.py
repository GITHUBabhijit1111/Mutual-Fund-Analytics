from sqlalchemy import create_engine
import pandas as pd
import os

engine = create_engine("sqlite:///bluestock_mf.db")

folder = "data/processed"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        path = os.path.join(folder,file)

        df = pd.read_csv(path)

        table = file.replace(".csv","")

        df.to_sql(table,
                  engine,
                  if_exists="replace",
                  index=False)

        print(f"{table} loaded successfully")

print("Database Created Successfully")
