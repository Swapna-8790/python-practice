from sklearn.decomposition import PCA

x=[
    [10,20],
    [20,40],
    [30,60],
    [40,80]
]

pca=PCA(n_components=1)
result=pca.fit_transform(x)

print(result.shape[1])
