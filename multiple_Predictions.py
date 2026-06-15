from sklearn.linear_model import LogisticRegression

x=[[1],[2],[3],[4],[5]]
y=[0,0,0,1,1]

model=LogisticRegression()
model.fit(x,y)

print(model.predict(
      [[2],[4],[5]]
      )
)