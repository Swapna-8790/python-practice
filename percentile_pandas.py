import pandas as pd
data={
    "marks":[50,60,70,80,90,100]
}
df=pd.DataFrame(data)

print(df["marks"].quantile(0.25))
print(df["marks"].quantile(0.50))
print(df["marks"].quantile(0.75))