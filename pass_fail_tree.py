from sklearn.tree import DecisionTreeClassifier

hours=[[1],[2],[3],[4],[5],[6]]
result=[0,0,0,1,1,1]

model=DecisionTreeClassifier()
model.fit(hours,result)

print(model.predict([[5]]))