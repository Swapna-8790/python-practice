from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

x=[[1],[2],[3],[4],[5],[6]]
y=[20,40,60,80,100,120]

x_train,x_test,y_train,y_test=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

model=LinearRegression()
model.fit(x_train,y_train)

predictions=model.predict(x_test)

print("actual")
print(y_test)

print("predicted")
print(predictions)