import sqlite3

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("bluestock_mf.db")

# Read schema.sql
with open("sql/schema.sql", "r") as f:
    schema = f.read()

# Execute schema
conn.executescript(schema)

conn.commit()
conn.close()

print("✅ Database and tables created successfully!")