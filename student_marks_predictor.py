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

hours = int(input("Study Hours: "))

prediction = model.predict([[hours]])

print("Expected Marks:",prediction[0])