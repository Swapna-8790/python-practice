from sklearn.preprocessing import StandardScaler

data=[
    [1],
    [2],
    [3],
    [4],
    [5]
]
model=StandardScaler()
print(model.fit_transform(data))