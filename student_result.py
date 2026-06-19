from sklearn.naive_bayes import GaussianNB

X = [[25], [35], [45], [55], [65]]
y = [0, 0, 0, 1, 1]

model = GaussianNB()
model.fit(X, y)

marks = int(input("Enter Marks: "))

prediction = model.predict(
    [[marks]]
)

if prediction[0] == 1:
    print("Pass")
else:
    print("Fail")