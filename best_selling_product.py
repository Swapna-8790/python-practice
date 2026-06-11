import pandas as pd
df=pd.read_csv("supermarket_sales.csv")

result=df.groupby("Product")["Quantity"].sum()
print(result)

print("best selling product")
print(result.idxmax())
