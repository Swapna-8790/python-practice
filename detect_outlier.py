import numpy as np
marks=[50,60,70,80,90,100,300]

q1=np.percentile(marks,25)
q3=np.percentile(marks,75)

iqr=q3-q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

print("lower limit=",lower)
print("upper limit=",upper)

for i in marks:
    if i < lower or i > upper:
        print("outlier=",i)
