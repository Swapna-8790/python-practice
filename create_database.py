import sqlite3
conn=sqlite3.connect("student.db")

print("database created")

conn.close()