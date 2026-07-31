from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///bluestock_mf.db")

tables = pd.read_sql(
"""
SELECT name
FROM sqlite_master
WHERE type='table'
""",
engine)

print(tables)

for table in tables["name"]:

    count = pd.read_sql(
        f"SELECT COUNT(*) AS rows FROM {table}",
        engine
    )

    print(table)
    print(count)