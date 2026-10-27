## UPDATE & SET

"""
    Day 6 — Question 4: 
    1. Increase every employee's salary by 5%.
"""

import sqlite3

conn = sqlite3.connect("DataAnalytics.db")
cursor = conn.cursor()

cursor.execute("""
    UPDATE EMP
    SET Salary = Salary*1.05
""")

conn.commit()

cursor.execute("""
    SELECT * FROM EMP
""")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()

