import pandas as pd
df = pd.read_csv("supermarket_sales.csv")
df["Revenue"] = df["Quantity"] * df["Price"]

print("SUPERMARKET SALES REPORT")
print("-" * 30)

print("Total Revenue")
print(df["Revenue"].sum())

print("\nAverage Revenue")
print(df["Revenue"].mean())

print("\nBest Selling Product")
print(
    df.groupby("Product")["Quantity"]
      .sum()
      .idxmax()
)

print("\nHighest Revenue Product")
print(
    df.groupby("Product")["Revenue"]
      .sum()
      .idxmax()
)

print("\nBest Category")
print(
    df.groupby("Category")["Revenue"]
      .sum()
      .idxmax()
)