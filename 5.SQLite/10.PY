# TRANSACTION & ROLLBACK

"""
    Day 6 — Question 5
    Update the salary of John by ₹2,000 and Black by ₹5,000. If the total salary exceeds ₹50,000, undo the update.
"""

import sqlite3 

conn = sqlite3.connect("DataAnalytics.db")
cursor = conn.cursor()

cursor.execute("BEGIN TRANSACTION")

cursor.execute("""
    UPDATE EMP 
    SET Salary = Salary+2000
    WHERE Empname = "John"
""")

cursor.execute("""
    UPDATE EMP 
    SET Salary = Salary+5000
    WHERE Empname = "Black"
""")

cursor.execute("""
    SELECT SUM(Salary)
    FROM EMP
    WHERE Empname IN ("John","Black")
""")
sum = cursor.fetchone()[0]

if sum>50000:
    conn.rollback()
else:
    conn.commit()

cursor.close()
conn.close()

