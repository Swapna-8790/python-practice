import pandas as pd
df=pd.read_csv("sales_data.csv")
result=df.groupby("Department")["Sales"].agg(
    ["sum","mean","max","min"]
)
print(result)