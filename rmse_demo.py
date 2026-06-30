from sklearn.metrics import mean_squared_error

y_true=[100,200,300,400]
y_pred=[110,190,310,380]

mse=mean_squared_error(
    y_true,
    y_pred
)

rmse=mse**0.5

print("RMSE:",rmse)