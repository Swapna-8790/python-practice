from sklearn.linear_model import LinearRegression
import pandas as pd

data = {
    "Area":[800,1000,1200,1400,1600],
    "Bedrooms":[2,2,3,3,4],
    "Price":[20,25,30,35,40]
}

df = pd.DataFrame(data)

X = df[["Area","Bedrooms"]]
y = df["Price"]

model = LinearRegression()
model.fit(X,y)

prediction = model.predict([[1800,4]])

print(prediction[0])