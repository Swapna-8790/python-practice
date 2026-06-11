import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("supermarket_sales.csv")

df["Revenue"]=df["Quantity"] *df["Price"]
category_revenue=df.groupby("Category")["Revenue"].sum()

category_revenue.plot(kind="bar")
plt.title("Revenue by Category")
plt.show()