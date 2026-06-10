import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV file
df = pd.read_csv("students.csv")

# Display student data
print("Student Data")
print(df)

# Create Total column
df["Total"] = df["Maths"] + df["Science"] + df["English"]

print("\nTotal Marks")
print(df[["Name", "Total"]])

# Find top student
top_student = df.loc[df["Total"].idxmax()]

print("\nTop Student")
print(top_student)

# Create graph
sns.barplot(x="Name", y="Total", data=df)

plt.title("Student Total Marks")

plt.show()