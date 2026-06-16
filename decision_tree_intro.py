from sklearn.tree import DecisionTreeClassifier

x=[[1],[2],[3],[4],[5]]
y=[0,0,0,1,1]

model=DecisionTreeClassifier()
model.fit(x,y)

print(model.predict([[4]]))