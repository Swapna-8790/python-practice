from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

X = [[1],[2],[3],[4],[5]]
y = [0,0,0,1,1]

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

params = {
    "model__C":[0.1,1,10]
}

grid = GridSearchCV(
    pipe,
    params,
    cv=2
)

grid.fit(X,y)

print(grid.best_params_)