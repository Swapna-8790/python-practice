import pandas as pd
df=pd.read_csv("students.csv")

print("maths average")
print(df["Maths"].mean())

print("science average")
print(df["Science"].mean())

print("english average")
print(df["English"].mean())