import pandas as pd
df=pd.read_csv("supermarket_sales.csv")

df["Revenue"]=df["Quantity"] *df["Price"]

print("Average order revenue")
print(df["Revenue"].mean())
