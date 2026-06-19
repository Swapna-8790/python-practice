from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import cross_val_score

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1]

lr = LogisticRegression()
dt = DecisionTreeClassifier()

lr_score = cross_val_score(
    lr,
    X,
    y,
    cv=2
)

dt_score = cross_val_score(
    dt,
    X,
    y,
    cv=2
)

print("Logistic:",lr_score.mean())

print("Decision Tree:",dt_score.mean())