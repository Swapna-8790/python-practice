from sklearn.cluster import AgglomerativeClustering
x=[
    [1],
    [2],
    [3],
    [10],
    [11],
    [12]
    ]
model=AgglomerativeClustering(
    n_clusters=2
)
labels=model.fit_predict(x)

print("data points: ",len(x))
print("clusters:",len(set(labels)))