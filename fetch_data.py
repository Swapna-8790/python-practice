import sqlite3
conn=sqlite3.connect("student.db")

cursor=conn.cursor()

cursor.execute(
    "SELECT * FROM Students"           
)

rows=cursor.fetchall()

for row in rows:
    print(row)

conn.close()