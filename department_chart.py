import pandas as pd
import matplotlib.pyplot as plt

employees=pd.read_csv("employees.csv")
departments=pd.read_csv("departments.csv")

data=pd.merge(
    employees,
    departments,
    on="DepartmentID"
)
result=data.groupby("DepartmentName")["EmpID"].count()
result.plot(kind="bar")

plt.title("employees per department")
plt.show()
