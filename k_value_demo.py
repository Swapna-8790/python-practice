from sklearn.neighbors import KNeighborsClassifier

x=[[1],[2],[3],[4],[5],[6]]
y=[0,0,0,1,1,1]

model=KNeighborsClassifier(
    n_neighbors=5
)
model.fit(x,y)

print(model.predict([[4]]))
