import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("employees.csv")
plt.bar(df["Name"],df["Salary"])

plt.title("employee salaries")
plt.xlabel("employees")
plt.ylabel("salary")
plt.show()
