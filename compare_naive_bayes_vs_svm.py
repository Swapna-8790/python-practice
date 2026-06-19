from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1]

nb = GaussianNB()
svm = SVC()

nb.fit(X, y)
svm.fit(X, y)

print("Naive Bayes:",nb.predict([[4]])[0])
print("SVM:",svm.predict([[4]])[0])