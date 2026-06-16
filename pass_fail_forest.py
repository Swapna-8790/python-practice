from sklearn.ensemble import RandomForestClassifier

hours = [[1], [2], [3], [4], [5], [6]]
result = [0, 0, 0, 1, 1, 1]

model = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)

model.fit(hours, result)

print(
    model.predict([[5]])
)