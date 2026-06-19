from sklearn.svm import SVC

x=[[1],[2],[3],[4],[5]]
y=[0,0,0,1,1]

model=SVC()
model.fit(x,y)

print(model.predict([[4]]))
