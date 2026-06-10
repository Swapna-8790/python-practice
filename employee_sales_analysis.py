import pandas as pd
df = pd.read_csv("sales_data.csv")

print("Total Sales")
print(df["Sales"].sum())

print("\nAverage Sales")
print(df["Sales"].mean())

print("\nBest Employee")
top = df.loc[df["Sales"].idxmax()]
print(top)