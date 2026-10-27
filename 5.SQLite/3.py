# sqlite boilerplate practice

import sqlite3

conn = sqlite3.connect("Database2.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS emp(
        emp_id INEGER PRIMARY KEY,
        emp_name TEXT NOT NULL,
        salary INTEGER NOT NULL
    )
""")

cursor.execute("INSERT INTO emp VALUES(?,?,?)",(9109,"Elon Musk",1000000))
cursor.execute("INSERT INTO emp VALUES(?,?,?)",(9110,"Jeff Bejos",900000))
cursor.execute("INSERT INTO emp VALUES(?,?,?)",(9111,"Mark Zuckerberg",800000))

conn.commit()

cursor.execute("SELECT * FROM emp")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()