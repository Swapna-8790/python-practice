import pandas as pd
df=pd.read_csv("employees.csv")
df=df.drop("Experience",axis=1)
print(df)