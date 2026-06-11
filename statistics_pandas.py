import pandas as pd
data={
    "marks":[70,80,80,90,100]
}
df=pd.DataFrame(data)

print(df["marks"].mean())
print(df["marks"].median())
print(df["marks"].mode())

