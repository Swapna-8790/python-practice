import pandas as pd
df=pd.read_csv("supermarket_sales.csv")

df["Revenue"]=df["Quantity"] * df["Price"]

result=df.groupby("Category")["Revenue"].sum()
print(result)
