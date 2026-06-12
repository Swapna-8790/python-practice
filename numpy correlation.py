import numpy as np

hours=[1,2,3,4,5]
marks=[20,40,60,80,100]

corr=np.corrcoef(hours,marks)
print(corr)