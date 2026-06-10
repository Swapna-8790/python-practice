import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
sales = df.groupby("Department")["Sales"].sum()

sales.plot(kind="bar")

plt.title("Department Sales")
plt.show()