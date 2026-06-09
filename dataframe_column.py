import pandas as pd
data={
    "name":["swapna","rahul"],
    "age":[20,21]
}
df=pd.DataFrame(data)
print(df["name"])