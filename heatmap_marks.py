import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("students.csv")

data=df[["Maths","Science","English"]]
sns.heatmap(data,annot=True)
plt.title("student markks heatmap")
plt.show()