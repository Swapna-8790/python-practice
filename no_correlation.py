import pandas as pd
data={
    "age":[10,20,30,40,50],
    "luckynumber":[7,2,9,1,5]
}
df=pd.DataFrame(data)
print(df.corr())