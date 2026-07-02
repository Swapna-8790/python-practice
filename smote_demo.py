from sklearn.datasets import load_breast_cancer
from imblearn.over_sampling import SMOTE

data=load_breast_cancer()

x=data.data
y=data.target

print("BEFORE SMOTE:",x.shape)

smote=SMOTE(random_state=42)

x_resampled,y_resampled=smote.fit_resample(x,y)

print("AFTER SMOTE:",x_resampled.shape)