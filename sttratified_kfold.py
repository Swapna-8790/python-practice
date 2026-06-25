from sklearn.model_selection import StratifiedKFold

x=[[1],[2],[3],[4],[5],[6]]
y=[0,0,0,1,1,1]

skf=StratifiedKFold(
    n_splits=3
)

for train, test in skf.split(x,y):
    print("Train:", train)
    print("Test :", test)
    print()