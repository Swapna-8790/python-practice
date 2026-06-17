from sklearn.cluster import KMeans

spending = [
    [1000],
    [1200],
    [1500],
    [8000],
    [8500],
    [9000]
]

model = KMeans(
    n_clusters=2,
    random_state=42
)

model.fit(spending)

print(model.labels_)