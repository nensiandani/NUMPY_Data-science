import numpy as np

arr =np.array([1.4,2.6,5.9])
print(arr.dtype)

int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)

'''
float64
[1 2 5]
int64

'''