from sklearn.svm import SVC

X = [[25], [35], [45], [55], [65]]
y = [0, 0, 0, 1, 1]

model = SVC()
model.fit(X, y)

marks = int(input("Enter Marks: "))

prediction = model.predict([[marks]])

if prediction[0] == 1:
    print("Pass")
else:
    print("Fail")