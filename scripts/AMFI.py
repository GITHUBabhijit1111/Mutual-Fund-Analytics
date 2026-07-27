import pandas as pd

master = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(master["amfi_code"])
nav_codes = set(nav["amfi_code"])

missing = master_codes - nav_codes

print("Total AMFI codes in fund_master:", len(master_codes))
print("Total AMFI codes in nav_history:", len(nav_codes))
print("Missing codes:", len(missing))

if missing:
    print("Missing AMFI Codes:")
    print(missing)
else:
    print("All AMFI codes are present.")