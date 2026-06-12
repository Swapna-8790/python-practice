import numpy as np
data1=[78,79,80,81,82]
data2=[20,50,80,110,140]

q1_1=np.percentile(data1,25)
q3_1=np.percentile(data1,75)

q1_2=np.percentile(data2,25)
q3_2=np.percentile(data2,75)

print("IQR dataset1=",q3_1-q1_1)
print("IQR dataset2=",q3_2-q1_2)




