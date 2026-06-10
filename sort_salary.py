import pandas as pd
df=pd.read_csv("employees.csv")
print(df.sort_values("Salary"))