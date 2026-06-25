import pandas as pd

df=pd.DataFrame({
    "age":[20,None,25,30]
})

print(df)

df["age"]=df["age"].fillna(df["age"].mean())

print("\nAfter filling missing values:")
print(df)