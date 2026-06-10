import pandas as pd
df=pd.read_csv("sales.csv")
high_sales=df[df["Units_Sold"]>20]
print(high_sales)