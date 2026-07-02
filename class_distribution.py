from sklearn.datasets import load_breast_cancer
import pandas as pd

data = load_breast_cancer()

df = pd.DataFrame(data.data)
df["Target"] = data.target

print(df["Target"].value_counts())