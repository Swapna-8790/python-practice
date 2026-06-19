from sklearn.cluster import AgglomerativeClustering
import pandas as pd

data = {
    "Salary": [
        25000,
        28000,
        30000,
        70000,
        75000,
        80000
    ]
}
df = pd.DataFrame(data)

model = AgglomerativeClustering(
    n_clusters=2
)

labels = model.fit_predict(df)
print(labels)