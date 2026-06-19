from sklearn.cluster import AgglomerativeClustering
import pandas as pd

data={
    "marks":[35,40,45,85,90,95]
}
df=pd.DataFrame(data)
model=AgglomerativeClustering(
    n_clusters=2
)
print(model.fit_predict(df))