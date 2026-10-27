"""
    Question 2 — Delete records
    Delete all employees whose commission is NULL and whose department ID is not 1, 2, or 3.
"""

import sqlite3

conn = sqlite3.connect("DataAnalytics.db")
cursor = conn.cursor()

cursor.execute("""
    DELETE FROM EMP
    WHERE Commission IS NULL
     AND Deptid NOT IN (1,2,3)
""")

conn.commit()

cursor.execute("SELECT * FROM EMP")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()