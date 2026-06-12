import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data={
    "hours":[1,2,3,4,5],
    "marks":[20,40,60,80,100],
    "attendance":[60,70,80,90,100]
}

df=pd.DataFrame(data)

sns.heatmap(df.corr(),annot=True)

plt.show()