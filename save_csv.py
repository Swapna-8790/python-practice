import pandas as pd
data={
    "name":["swapna","rahul"],
    "age":[20,21]
}
df=pd.DataFrame(data)
df.to_csv("student.csv",index=False)
print("csv saved")