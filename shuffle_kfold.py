from sklearn.model_selection import KFold

kf = KFold(
    n_splits=3,
    shuffle=True,
    random_state=42
)

for train, test in kf.split(
    [1,2,3,4,5,6]
):
    print("Train:", train)
    print("Test :", test)
    print()