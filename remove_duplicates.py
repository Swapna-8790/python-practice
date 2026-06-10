import pandas as pd
df=pd.read_csv("employees_dirty.csv")
df=df.drop_duplicates()
print(df)