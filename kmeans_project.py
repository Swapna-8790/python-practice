from sklearn.cluster import KMeans

scores = [
    [30],
    [35],
    [40],
    [75],
    [80],
    [85]
]

model = KMeans(
    n_clusters=2,
    random_state=42
)

model.fit(scores)

print("Clusters")
print(model.labels_)

print("\nCenters")
print(model.cluster_centers_)