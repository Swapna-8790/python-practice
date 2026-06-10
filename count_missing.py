import pandas as pd
df=pd.read_csv("employees_dirty.csv")
print(df.isnull().sum())