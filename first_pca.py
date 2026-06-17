from sklearn.decomposition import PCA

x=[
    [1,2],
    [2,4],
    [3,6],
    [4,8]
]

model=PCA(n_components=1)
print(model.fit_transform(x))
