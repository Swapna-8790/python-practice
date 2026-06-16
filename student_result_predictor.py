from sklearn.tree import DecisionTreeClassifier

hours = [[1], [2], [3], [4], [5], [6]]
result = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier()

model.fit(hours, result)

study_hours = int(input("Hours Studied: "))

prediction = model.predict(
    [[study_hours]]
)

if prediction[0] == 1:
    print("Pass")
else:
    print("Fail")