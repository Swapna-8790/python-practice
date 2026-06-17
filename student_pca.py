from sklearn.decomposition import PCA
import pandas as pd

data={
    "math":[80,70,90,60],
    "science":[82,72,91,62]
}
df=pd.DataFrame(data)

pca=PCA(n_components=1)
print(pca.fit_transform(df))
