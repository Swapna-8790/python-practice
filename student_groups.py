from sklearn.cluster import KMeans

marks = [
    [35],
    [40],
    [45],
    [75],
    [80],
    [85]
]

model = KMeans(
    n_clusters=2,
    random_state=42
)

model.fit(marks)

print(model.labels_)