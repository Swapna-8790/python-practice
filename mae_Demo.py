from sklearn.metrics import mean_absolute_error

y_true=[100,200,300,400]
y_pred=[110,190,310,380]

mae=mean_absolute_error(
    y_true,
    y_pred
)

print("MAE:",mae)