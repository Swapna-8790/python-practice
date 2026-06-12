import numpy as np
marks=[50,60,70,80,90,100]

q1=np.percentile(marks,25)
q3=np.percentile(marks,75)

iqr=q3-q1
print("IQR=",iqr)