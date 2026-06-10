import pandas as pd
df=pd.read_csv("employees_dirty.csv")
df["Salary"]=df["Salary"].fillna(45000)
df=df.drop_duplicates()
print(df)