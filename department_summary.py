import pandas as pd
employees=pd.read_csv("employees.csv")
departments=pd.read_csv("departments.csv")

data=pd.merge(
    employees,
    departments,
    on="DepartmentID"
)

print(data)
