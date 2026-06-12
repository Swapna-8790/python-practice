from sklearn.linear_model import LinearRegression
import pandas as pd

data = {
    "Area": [500, 700, 900, 1100, 1300],
    "Price": [10, 15, 20, 25, 30]
}

df = pd.DataFrame(data)

X = df[["Area"]]
y = df["Price"]

model = LinearRegression()

model.fit(X, y)

print(
    model.predict([[1500]])
)