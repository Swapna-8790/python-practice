from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import RandomizedSearchCV

x=[[1],[2],[3],[4],[5]]
y=[0,0,0,1,1]

params={
    "max_depth":[1,2,3,4,5]
}

search=RandomizedSearchCV(
    DecisionTreeClassifier(),
    params,
    n_iter=3,
    cv=2,
    random_state=42
)

search.fit(x,y)

print(search.best_params_)