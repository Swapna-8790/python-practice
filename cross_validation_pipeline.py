from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

X = [[1],[2],[3],[4],[5]]
y = [0,0,0,1,1]

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

scores = cross_val_score(
    pipe,
    X,
    y,
    cv=2
)

print(scores)