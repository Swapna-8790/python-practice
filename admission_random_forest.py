from sklearn.ensemble import RandomForestClassifier

marks = [[40], [50], [60], [70], [80], [90]]
admission = [0, 0, 0, 1, 1, 1]

model = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)

model.fit(marks, admission)

score = int(input("Marks: "))

prediction = model.predict(
    [[score]]
)

if prediction[0] == 1:
    print("Selected")
else:
    print("Rejected")