from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

X = [[10], [20], [30], [40], [50]]
y = [0, 0, 0, 1, 1]

model = RandomForestClassifier(
    n_estimators=20,
    random_state=42
)

scores = cross_val_score(
    model,
    X,
    y,
    cv=2
)

print("Scores:")
print(scores)

print("Average:",scores.mean())