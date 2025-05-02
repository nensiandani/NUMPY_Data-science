import numpy as np

arr = np.array([1,2,np.inf,4,-np.inf,6])

print(np.isinf(arr))

clear = np.nan_to_num(arr,posinf=1000,neginf=-1000)

print(clear)

'''
[False False  True False  True False]
[    1.     2.  1000.     4. -1000.     6.]

'''