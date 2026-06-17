
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

x=[[1],[2],[3],[4],[5],[6]]
y=[0,0,0,1,1,1]

x_train,x_test,y_train,y_test=train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

model=StandardScaler()

x_train=model.fit_transform(x_train)
x_test=model.transform(x_test)

print("train")
print(x_train)

print("test")
print(x_test)
