from sklearn.preprocessing import MinMaxScaler

data=[
    [100],
    [200],
    [300],
    [400],
    [500]
]
scaler=MinMaxScaler()
scaled=scaler.fit_transform(data)

print("original")
print(data)

print("\nscaled")
print(scaled)