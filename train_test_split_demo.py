from sklearn.model_selection import train_test_split

x=[[1],[2],[3],[4],[5],[6],[7],[8]]
y=[10,20,30,40,50,60,70,80]

x_train,x_test,y_train,y_test=train_test_split(
    x,
    y,
    test_size=0.25,
    random_state=42
)
print("training data")
print(x_train)

print("\ntesting data")
print(x_test)
