from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

X = [[10], [20], [30], [40], [50]]
y = [0, 0, 0, 1, 1]

model = GaussianNB()
model.fit(X, y)

predictions = model.predict(X)

print("Accuracy:")
print(
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