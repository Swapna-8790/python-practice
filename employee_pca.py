from sklearn.decomposition import PCA
import pandas as pd

data = {
    "Experience": [1, 2, 3, 4],
    "Salary": [30000, 40000, 50000, 60000]
}

df = pd.DataFrame(data)

pca = PCA(n_components=1)

result = pca.fit_transform(df)
print(result)