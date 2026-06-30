from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score

data = load_breast_cancer()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

lr = LogisticRegression(max_iter=10000)
dt = DecisionTreeClassifier()

lr.fit(X_train, y_train)
dt.fit(X_train, y_train)

lr_score = roc_auc_score(
    y_test,
    lr.predict_proba(X_test)[:,1]
)

dt_score = roc_auc_score(
    y_test,
    dt.predict_proba(X_test)[:,1]
)

print("Logistic Regression:", lr_score)
print("Decision Tree:", dt_score)