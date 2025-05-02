import numpy as np

arr = np.array([1,2,np.nan,4,np.nan,6])


result = np.nan_to_num(arr)
result1 = np.nan_to_num(arr,nan=100)
print(result)
print(result1)

'''
[1. 2. 0. 4. 0. 6.]

[  1.   2. 100.   4. 100.   6.]

'''