from sklearn.naive_bayes import GaussianNB

X = [[50], [60], [70], [80], [90]]
y = [0, 0, 1, 1, 1]

model = GaussianNB()
model.fit(X, y)

print(model.predict([[75]]))