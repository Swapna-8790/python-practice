from sklearn.preprocessing import LabelEncoder

data=[
    "red",
    "blue",
    "green",
    "red"
]

encoder=LabelEncoder()

result=encoder.fit_transform(data)
print(result)