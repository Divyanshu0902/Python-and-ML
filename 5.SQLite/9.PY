# 2. ORDER BY __ DESC/ASC | LIMIT __

"""
Day 6 — Question 4: 
    2. Display the five highest-paid employees
"""

import sqlite3

conn = sqlite3.connect("DataAnalytics.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT Empid, Empname, Salary
    FROM EMP
    ORDER BY Salary DESC
    LIMIT 5
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()