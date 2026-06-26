from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

X = [[1],[2],[3],[4],[5]]
y = [0,0,0,1,1]

params = {
    "max_depth":[1,2,3],
    "criterion":["gini","entropy"]
}

grid = GridSearchCV(
    DecisionTreeClassifier(),
    params,
    cv=2
)

grid.fit(X,y)

print("Best Parameters:",
      grid.best_params_)

print("Best Score:",
      grid.best_score_)