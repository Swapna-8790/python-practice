from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1]

model = SVC()
model.fit(X, y)

predictions = model.predict(X)

print(
    accuracy_score(
        y,
        predictions
    )
)