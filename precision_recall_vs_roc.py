from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    precision_score,
    recall_score,
    roc_auc_score
)

data = load_breast_cancer()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

predictions= model.predict(X_test)
probability = model.predict_proba(X_test)[:,1]

print("Precision :", precision_score(y_test,predictions))
print("Recall    :", recall_score(y_test,predictions))
print("ROC-AUC   :", roc_auc_score(y_test, probability))