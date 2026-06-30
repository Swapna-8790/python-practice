from sklearn.metrics import r2_score

y_true=[100,200,300,400]
y_pred=[110,190,310,380]

score=r2_score(
    y_true,
    y_pred
)

print("R2 SCORE:",score)