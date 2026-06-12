from sklearn.linear_model import LinearRegression
import pandas as pd

data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [25000, 35000, 45000, 55000, 65000]
}
df = pd.DataFrame(data)

X = df[["Experience"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)

years = int(input("Experience: "))

prediction = model.predict([[years]])
print("Predicted Salary:",prediction[0])