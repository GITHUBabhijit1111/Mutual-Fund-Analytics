import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Columns:")
print(df.columns)

print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nUnique Categories:")
print(df["category"].unique())

print("\nUnique Sub Categories:")
print(df["sub_category"].unique())

print("\nUnique Risk Grades:")
print(df["risk_category"].unique())   # Change if your column name is different