## SQLite Boilerplate : 

import sqlite3

conn = sqlite3.connect("DataAnalytics.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS EMP (
        Empid INTEGER PRIMARY KEY,
        Empname TEXT NOT NULL,
        Salary INTEGER NOT NULL CHECK (Salary > 5000),
        Commission REAL,
        Deptid TEXT NOT NULL
    )
""")

conn.commit()
conn.close()