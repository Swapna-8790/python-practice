from sklearn.cluster import AgglomerativeClustering
x=[
    [5],
    [6],
    [7],
    [50],
    [60],
    [70]
    ]
model=AgglomerativeClustering(
    n_clusters=2
)
labels=model.fit_predict(x)

for value,label in zip(x,labels):
    print(value[0],"-> Group",label)