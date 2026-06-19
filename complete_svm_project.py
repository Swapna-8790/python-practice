from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X = [[10], [20], [30], [40], [50]]
y = [0, 0, 0, 1, 1]

model = SVC()
model.fit(X, y)

predictions = model.predict(X)

print(
    "Accuracy:",
    accuracy_score(
        y,
        predictions
    )
)

score = int(input("Enter Score: "))

result = model.predict([[score]])

if result[0] == 1:
    print("Selected")
else:
    print("Rejected")