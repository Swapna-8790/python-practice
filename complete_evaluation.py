from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

X = [[1], [2], [3], [4], [5], [6]]
y = [20, 40, 60, 80, 100, 120]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual Values")
print(y_test)

print("\nPredicted Values")
print(predictions)

print(
    "\nMAE:",
    mean_absolute_error(
        y_test,
        predictions
    )
)