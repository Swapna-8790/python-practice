import pandas as pd
df=pd.read_csv("employees.csv")
it_emp=df[df["Department"]=="IT"]
print(it_emp)

print("\nAverage IT Salary")
print(it_emp["Salary"].mean())