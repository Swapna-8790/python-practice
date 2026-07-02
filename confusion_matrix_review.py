from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

data = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(
    data.data,
    data.target,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(confusion_matrix(y_test, predictions))