import sqlite3 

conn = sqlite3.connect("DataAnalytics.db")
cursor = conn.cursor()

cursor.execute("""

""")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()