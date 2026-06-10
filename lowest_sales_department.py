import pandas as pd
df=pd.read_csv("sales_data.csv")
result=df.groupby("Department")["Sales"].min()
print(result)