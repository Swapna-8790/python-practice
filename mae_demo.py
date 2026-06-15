from sklearn.metrics import mean_absolute_error

actual=[100,200,300]
predicted=[110,190,320]

mae=mean_absolute_error(
    actual,
    predicted,
)
print(mae)