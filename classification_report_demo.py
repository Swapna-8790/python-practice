from sklearn.metrics import classification_report

y_true=[1,0,1,1,0]
y_pred=[1,0,1,0,0]

classification=classification_report(
    y_true,
    y_pred
)

print(classification)