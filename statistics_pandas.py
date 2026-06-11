import pandas as pd

data={
    "marks":[60,70,80,90,100]
}
df=pd.DataFrame(data)

print("variance")
print(df["marks"].var())          

print("\nstandard deviation")
print(df["marks"].std())                  