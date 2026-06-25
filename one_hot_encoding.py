import pandas as pd

df=pd.DataFrame({
    "color":[
        "red",
        "blue",
        "green"
    ]
})

encoded=pd.get_dummies(
    df,
    columns=["color"]

)

print(encoded)