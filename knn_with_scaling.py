from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

x=[[1],[2],[3],[4],[5],[6]]
y=[0,0,0,1,1,1]

scaler=StandardScaler()
x_scaled=scaler.fit_transform(x)

model=KNeighborsClassifier(
    n_neighbors=3
)
model.fit(x_scaled,y)

prediction=model.predict(
    scaler.transform([[7]])
)
print(prediction)
