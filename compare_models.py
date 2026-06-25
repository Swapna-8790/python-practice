from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import numpy as np

X = [[1],[2],[3],[4],[5]]
y = [0,0,0,1,1]

dt = DecisionTreeClassifier()

lr = LogisticRegression()

dt_score = cross_val_score(
    dt,
    X,
    y,
    cv=2
)

lr_score = cross_val_score(
    lr,
    X,
    y,
    cv=2
)

print("Decision Tree Mean:",
      np.mean(dt_score))

print("Logistic Regression Mean:",
      np.mean(lr_score))