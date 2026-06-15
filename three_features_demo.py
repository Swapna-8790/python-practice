from sklearn.linear_model import LinearRegression
import pandas as pd

data = {
    "Hours": [1, 2, 3, 4, 5],
    "Attendance":[60,70,75,85,95],
    "Assignments":[1,2,3,4,5],
    "Marks": [20, 40, 60, 80, 100]
}

df = pd.DataFrame(data)

X = df[["Hours","Attendance","Assignments"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[6,100,6]])

print(prediction)