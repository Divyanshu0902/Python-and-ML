### WHERE and HAVING
# WHERE filters individual rows before grouping.
# HAVING filters groups after aggregation.

"""
    Day 6 — Question 3: Department statistics

    Find the average salary and employee count for each department, 
    then insert those results into a table named DEPARTMENT with these columns:
    - Deptid - NumberOfEmployees - AvgSalary
    Do not insert departments whose average salary is below ₹12,000.
"""

import sqlite3 

conn = sqlite3.connect("DataAnalytics.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS DEPARTMENT(
        Deptid INTEGER PRIMARY KEY,
        NoOfEmployees INTEGER NOT NULL,
        AverageSalary REAL NOT NULL
    );
""")

cursor.execute("""
    INSERT INTO DEPARTMENT (Deptid, NoOfEmployees, AverageSalary)
        SELECT Deptid, 
            COUNT(*),
            AVG(Salary)
        FROM EMP
        GROUP BY Deptid
        HAVING AVG(Salary) >= 12000;
""")

conn.commit()


cursor.execute("""
    SELECT * FROM DEPARTMENT
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()