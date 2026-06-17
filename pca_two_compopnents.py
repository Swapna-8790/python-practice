from sklearn.decomposition import PCA

x=[
    [1,2],
    [2,4],
    [3,6],
    [4,8]
]

pca=PCA(n_components=2)
print(pca.fit_transform(x))
