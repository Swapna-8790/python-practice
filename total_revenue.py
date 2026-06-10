import pandas as pd
df=pd.read_csv("sales.csv")

df["Revenue"]=df["Units_Sold"]*df["Price"]
print(df)