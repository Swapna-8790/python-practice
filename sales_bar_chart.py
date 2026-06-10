import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("sales.csv")
df["Revenue"]=df["Units_Sold"]*df["Price"]
plt.bar(df["Product"],df["Revenue"])

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()