from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

x=[[1],[2],[3],[4],[5]]
y=[0,0,0,1,1]

params={
    "max_depth":[1,2,3]
}

grid=GridSearchCV(
    DecisionTreeClassifier(),
    params,
    cv=2
)

grid.fit(x,y)

print(grid.best_params_)