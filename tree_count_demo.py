from sklearn.ensemble import RandomForestClassifier

x=[[1],[2],[3],[4],[5],[6]]
y=[0,0,0,1,1,1]

model=RandomForestClassifier(
    n_estimators=50,
    random_state=42

)
model.fit(x,y)

print(model.predict([[4]]))