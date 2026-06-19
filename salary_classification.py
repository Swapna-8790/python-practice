from sklearn.naive_bayes import GaussianNB

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1]

model = GaussianNB()
model.fit(X, y)

years = int(input("Experience: "))

prediction = model.predict([[years]])

if prediction[0] == 1:
    print("High Salary")
else:
    print("Low Salary")