import pandas as pd
df=pd.read_csv("students.csv")
df["Average"]=(
    df["Maths"]+
    df["Science"]+
    df["English"]
)/3
print(df[["Name","Average"]])