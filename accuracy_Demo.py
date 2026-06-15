from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

x=[[1],[2],[3],[4],[5]]
y=[0,0,0,1,1]

model=LogisticRegression()
model.fit(x,y)

predictions=model.predict(x)
print(
    accuracy_score(
    y,
    predictions
))
