from sklearn.preprocessing import StandardScaler

from sklearn.preprocessing import MinMaxScaler

data=[
    [10],
    [20],
    [30],
    [40],
    [50]
]
model=StandardScaler()
print(model.fit_transform(data))

minmax=MinMaxScaler()
print(minmax.fit_transform(data))