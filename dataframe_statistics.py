import pandas as pd
data={
    "marks":[80,90,70,85,95]
}
df=pd.DataFrame(data)
print(df.describe())