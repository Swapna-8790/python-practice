import pandas as pd
df=pd.read_csv("employees.csv")
result=df[
    (df["Department"]=="IT") & (df["Salary"]>55000)
]
print(result)
