from sklearn.naive_bayes import GaussianNB

x=[[1],[2],[3],[4],[5]]
y=[0,0,0,1,1]

model=GaussianNB()
model.fit(x,y)

result=model.predict([[4]])
print(result)