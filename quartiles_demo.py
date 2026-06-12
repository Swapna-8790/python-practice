import numpy as np
marks=[50,60,70,80,90,100]

q1=np.percentile(marks,25)
q2=np.percentile(marks,50)
q3=np.percentile(marks,75)
print("Q1=",q1)
print("Q2=",q2)
print("Q3=",q3)