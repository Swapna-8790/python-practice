from sklearn.cluster import KMeans

x=[[1],
   [2],
   [3],
   [10],
   [11],
   [12],
   [20],
   [21],
   [22]
   ]

model=KMeans(
    n_clusters=3,
    random_state=42
)
model.fit(x)

print(model.labels_)