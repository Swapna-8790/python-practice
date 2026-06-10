import pandas as pd
df=pd.read_csv("sales_data.csv")
sales=df.groupby("Department")["Sales"].sum()
print("top department")
print(sales.idxmax())