import sqlite3
conn=sqlite3.connect("student.db")

cursor=conn.cursor()

data=[
    (2,'Anu',90),
    (3,'Rahul',75),
    (4,'Kiran',88)
]

cursor.executemany(
    "INSERT INTO Students VALUES(?,?,?)",data
)

conn.commit()

print("multiple rows inserted")

conn.close()