"""
    Aggregate Functions Application
"""

import sqlite3 

conn = sqlite3.connect("DataAnalytics.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT 
        Deptid, 
        Count(*) AS NoOfEmployees, 
        AVG(Salary) AS AverageSalary,
        MAX(Salary) AS MaximumSalary,
        MIN(Salary) AS MinimumSalary
    FROM EMP
    GROUP BY Deptid;
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()