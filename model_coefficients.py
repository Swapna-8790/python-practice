from sklearn.linear_model import LinearRegression
import pandas as pd

data = {
    "Experience": [1, 2, 3, 4, 5],
    "Skill":[2,3,5,6,8],
    "Salary": [25000,35000,45000,55000,65000]
}

df = pd.DataFrame(data)

X = df[["Experience","Skill"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)

print("coeffients")
print(model.coef_)

print("\nintercept")
print(model.intercept_)