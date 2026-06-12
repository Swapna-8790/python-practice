from sklearn.linear_model import LinearRegression
import pandas as pd

data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 60, 80, 100]
}
df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

print(
    model.predict([[6]])
)

print(
    model.predict([[10]])
)