import pandas as pd
employees=pd.read_csv("employees.csv")
departments=pd.read_csv("departments.csv")

data=pd.merge(
    employees,
    departments,
    on="DepartmentID"
)

print("total employees")
print(data["EmpID"].count())

print("\nDepartments")
print(data["DepartmentName"].unique())

print("\nemployees per department")
print(data.groupby("DepartmentName")["EmpID"].count())
