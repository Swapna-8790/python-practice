import sqlite3
conn=sqlite3.connect("student.db")

cursor=conn.cursor()

cursor.execute("""
UPDATE Students
SET marks=95
WHERE id=2 
""")

conn.commit()

print("data updated")

conn.close()
