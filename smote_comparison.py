from sklearn.datasets import load_breast_cancer
from imblearn.over_sampling import SMOTE
from collections import Counter

data = load_breast_cancer()

X = data.data
y = data.target

print("Before:", Counter(y))

smote = SMOTE(random_state=42)

X_resampled, y_resampled = smote.fit_resample(X, y)

print("After :", Counter(y_resampled))