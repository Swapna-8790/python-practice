from sklearn.cluster import AgglomerativeClustering
import pandas as pd

data={
    "score":[20,25,30,80,85,90]
}
df=pd.DataFrame(data)

model=AgglomerativeClustering(
    n_clusters=2
)
labels=model.fit_predict(df)

df["group"]=labels
print(df)