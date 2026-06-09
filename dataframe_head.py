import pandas as pd
data={
    "name":["A","B","C","D","E"],
    "age":[20,21,22,23,24]
}
df=pd.DataFrame(data)
print(df.head(3))