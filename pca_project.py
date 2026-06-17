from sklearn.decomposition import PCA
import pandas as pd

data = {
    "Math": [80, 70, 90, 60],
    "Science": [82, 72, 91, 62],
    "English": [78, 68, 88, 58]
}

df = pd.DataFrame(data)

pca = PCA(n_components=2)
result = pca.fit_transform(df)
print(result)