import pandas as pd
employees=pd.read_csv("employees.csv")
departments=pd.read_csv("departments.csv")

result=pd.merge(
    employees,
    departments,
    on="DepartmentID",
    how="left"
)
print(result)
