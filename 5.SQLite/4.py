# Day 6 — Question 1: Create the database and table

"""
create a database named DataAnalytics.db and an EMP table with these columns and constraints:
Column	Requirement
Empid	Integer, primary key
Empname	Varchar, cannot be NULL
Salary	Integer, cannot be NULL and must be greater than 5000
Commission	Float
Deptid	Integer, cannot be NULL
"""

import sqlite3 

conn = sqlite3.connect("DataAnalytics.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS EMP(
        Empid INTEGER PRIMARY KEY,
        Empname VARCHAR NOT NULL,
        Salary INTEGER NOT NULL CHECK(Salary>5000),
        Commission FLOAT,
        Deptid INTEGER NOT NULL
    )
""")

employees = [
    (101, "John",   25000, 1500.0, 1),
    (102, "Black",  18000, None,   2),
    (103, "Riya",   32000, 2500.0, 1),
    (104, "Aman",   14000, None,   4),
    (105, "Priya",  45000, 3000.0, 2),
    (106, "Rahul",  12000, None,   3),
    (107, "Neha",   28000, 1800.0, 3),
    (108, "Arjun",  16000, None,   4),
    (109, "Sneha",  55000, 4000.0, 1),
    (110, "Karan",  22000, 1200.0, 2)
]

cursor.executemany("""
    INSERT INTO EMP 
    (Empid, Empname, Salary, Commission, Deptid) 
    VALUES (?,?,?,?,?)
""", employees)

conn.commit()

cursor.execute("SELECT * FROM EMP")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()