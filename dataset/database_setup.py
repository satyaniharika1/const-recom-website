# dataset/database_setup.py
import sqlite3
try:
    import pandas as pd
except ImportError:
    print("Pandas is not installed. Please install it using 'pip install pandas'.")
    raise

# Connect to SQLite database
conn = sqlite3.connect("materials.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY,
    name TEXT,
    strength REAL,
    durability REAL,
    cost REAL
)
''')

# Load dataset
df = pd.read_csv("materials.csv")

# Insert data
df.to_sql("materials", conn, if_exists="replace", index=False)

# Commit and close
conn.commit()
conn.close()
print("Database setup completed.")
