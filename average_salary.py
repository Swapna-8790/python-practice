import pandas as pd
df=pd.read_csv("employees.csv")
print("average salary")
print(df["Salary"].mean())