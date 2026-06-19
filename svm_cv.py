from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1]

model = SVC()

scores = cross_val_score(
    model,
    X,
    y,
    cv=2
)

print(scores.mean())