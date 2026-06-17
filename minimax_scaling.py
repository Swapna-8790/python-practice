from sklearn.preprocessing import MinMaxScaler

data=[
    [10],
    [20],
    [30],
    [40],
    [50]
]
model=MinMaxScaler()
print(model.fit_transform(data))