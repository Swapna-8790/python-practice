import sqlite3
conn=sqlite3.connect("student.db")

cursor=conn.cursor()

cursor.execute("""
DELETE FROM Students
WHERE id=2 
""")

conn.commit()

print("Record deleted")

conn.close()
