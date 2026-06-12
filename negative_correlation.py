import pandas as pd
data={
    "tv_hours":[1,2,3,4,5],
    "marks":[100,80,60,40,20]
}
df=pd.DataFrame(data)
print(df.corr())