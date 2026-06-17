from sklearn.decomposition import PCA

x=[
    [1,2],
    [2,4],
    [3,6],
    [4,8]
]

pca=PCA(n_components=2)

pca.fit(x)

print(
    pca.explained_variance_ratio_
)
