from sklearn.preprocessing import StandardScaler
import pandas as pd

data={
    "Experience":[1,2,3,4,5],
    "Salary":[25000,35000,45000,55000,65000]
}
df=pd.DataFrame(data)

model=StandardScaler()
print(model.fit_transform(df))