import pandas as pd
data={
    "hours":[1,2,3,4,5],
    "marks":[20,40,60,80,100]
}
df=pd.DataFrame(data)
print(df.corr())