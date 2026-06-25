import sqlite3
conn=sqlite3.connect("student.db")

cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS
Students(
id INTEGER,
name TEXT,
marks INTEGER
)
""")

conn.commit()

print("table created")

conn.close()