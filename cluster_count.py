from sklearn.cluster import KMeans

marks = [
    [1],
    [2],
    [3],
    [10],
    [11],
    [12]
]

model = KMeans(
    n_clusters=2,
    random_state=42
)

model.fit(marks)

print(
    len(model.cluster_centers_)
)