from sklearn.metrics import recall_score

y_true=[1,0,1,1,0]
y_pred=[1,0,1,0,0]

recall=recall_score(
    y_true,
    y_pred
)

print(recall)