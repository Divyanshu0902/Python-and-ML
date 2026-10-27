# sample sqlite working --

import sqlite3

# 1. Connect to the database
conn = sqlite3.connect("Database1.db")

# 2. Create a cursor
cursor = conn.cursor()

# 3. Execute SQL to create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS EMP (
        Empid INTEGER PRIMARY KEY,
        Empname TEXT NOT NULL,
        Salary INTEGER NOT NULL
    )
""")

# 4. Insert a record
cursor.execute(
    "INSERT INTO EMP VALUES (?, ?, ?)",
    (101, "Riya", 25000)
)

# 5. Commit changes
conn.commit()

# 6. Retrieve records
cursor.execute("SELECT * FROM EMP")
rows = cursor.fetchall()

# 7. Display results
for row in rows:
    print(row)

# 8. Close resources
cursor.close()
conn.close()