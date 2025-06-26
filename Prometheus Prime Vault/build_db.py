import sqlite3

# Read the SQL file
with open('vault_schema.sql', 'r') as f:
    schema = f.read()

# Connect to a new SQLite database (or open it if it already exists)
conn = sqlite3.connect('prometheus_vault.db')
cursor = conn.cursor()

# Run the schema SQL commands to create the tables
cursor.executescript(schema)
conn.commit()
conn.close()

print("Database created and schema loaded successfully.")
