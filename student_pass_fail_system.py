from sklearn.linear_model import LogisticRegression

hours= [[1], [2], [3], [4], [5], [6]]
result= [0,0,0,1,1,1]


model = LogisticRegression()
model.fit(hours,result)

study_hours=int(input("hours studied: "))

prediction=model.predict(
    [[study_hours]]
)

if prediction[0]==1:
    print("pass")
else:
    print("fail")