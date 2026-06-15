from sklearn.linear_model import LogisticRegression

marks = [[40], [50], [60], [70], [80], [90]]
admission = [0, 0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(marks, admission)

score = int(input("Marks: "))

prediction = model.predict(
    [[score]]
)

if prediction[0] == 1:
    print("Selected")
else:
    print("Rejected")