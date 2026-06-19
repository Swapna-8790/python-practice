from sklearn.svm import SVC

X = [[50], [60], [70], [80], [90]]
y = [0, 0, 1, 1, 1]

model = SVC()
model.fit(X, y)

print(model.predict([[75]]))