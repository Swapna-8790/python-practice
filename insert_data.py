import sqlite3
conn=sqlite3.connect("student.db")

cursor=conn.cursor()

cursor.execute("""
INSERT INTO Students VALUES    
(1,'Ravi',85)
""")

conn.commit()

print("data inserted")

conn.close()