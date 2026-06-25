import sqlite3
import pandas as pd

conn=sqlite3.connect("student.db")

df=pd.read_sql(
    "SELECT * FROM Students",conn
)

print(df)

conn.close()