from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

x=[[1],[2],[3],[4],[5],[6]]
y=[0,0,0,1,1,1]

x_train,x_test,y_train,y_test=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

model=DecisionTreeClassifier()
model.fit(x_train,y_train)

predictions=model.predict(x_test)

print(
    accuracy_score(
        y_test,
        predictions
    )
)