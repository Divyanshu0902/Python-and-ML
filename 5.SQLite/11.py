"""
Day 6 — Question 6
The assignment asks you to accept an employee ID, increase that employee's salary by 5%, 
and display an appropriate message about whether the employee exists.
"""

emp_id = int(input("Enter the employee ID to look: "))

import sqlite3 

conn = sqlite3.connect("DataAnalytics.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT Empname 
    FROM EMP
    WHERE Empid = ?
""",(emp_id,))
employee = cursor.fetchone()

if employee == None:
    print("Employee does not exist.")
else:
    print("Employee Exists.")

    cursor.execute("""
        UPDATE EMP
        SET Salary = Salary*1.05
        WHERE Empid = ?
    """,(emp_id,))

cursor.close()
conn.close()