import pandas as pd
df=pd.read_csv("employees.csv")
highest=df.loc[df["Salary"].idxmax()]
print(highest)