import numpy as np
marks = np.array([85, 78, 92, 70, 88])

print("Average =", np.mean(marks))
print("Highest =", np.max(marks))
print("Lowest =", np.min(marks))

print("Students above 80")
print(marks[marks > 80])