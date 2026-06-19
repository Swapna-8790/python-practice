from sklearn.svm import SVC

x=[[20],[30],[40],[50],[60]]
y=[0,0,0,1,1]

model=SVC()
model.fit(x,y)

print(model.predict([[55]]))
