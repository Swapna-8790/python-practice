import pandas as pd
df=pd.read_csv("sales.csv")
df["Revenue"]=df["Units_Sold"]*df["Price"]
highest=df.loc[df["Revenue"].idxmax()]
print(highest)