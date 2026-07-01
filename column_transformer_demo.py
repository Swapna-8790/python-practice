import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

df = pd.DataFrame({
    "Age": [20, 25, 30],
    "Salary": [30000, 50000, 70000],
    "Gender": ["Male", "Female", "Male"]
})

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), ["Age", "Salary"]),
        ("cat", OneHotEncoder(), ["Gender"])
    ]
)

result = preprocessor.fit_transform(df)

print(result)