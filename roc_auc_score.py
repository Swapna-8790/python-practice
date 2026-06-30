from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

data = load_breast_cancer()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(
    max_iter=10000
)

model.fit(X_train, y_train)

probabilities = model.predict_proba(X_test)[:, 1]

score = roc_auc_score(
    y_test,
    probabilities
)

print("ROC-AUC Score:",score)