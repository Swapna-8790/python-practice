from sklearn.linear_model import LinearRegression
import pandas as pd

data={
    "hours":[1,2,3,4,5],
    "marks":[20,40,60,80,100]
}
df=pd.DataFrame(data)

x=df[["hours"]]
y=df["marks"]

model=LinearRegression()
model.fit(x,y)

prediction=model.predict([[6]])
print(prediction)