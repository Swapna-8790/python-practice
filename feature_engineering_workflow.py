import pandas as pd
from sklearn.preprocessing import LabelEncoder

df=pd.DataFrame({
    "gender":[
        "male",
        "female",
        "male"
    ]
})

encoder=LabelEncoder()

df["gender"]=encoder.fit_transform(df["gender"])

print(df)