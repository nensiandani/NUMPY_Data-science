import numpy as np 

a = np.array([[1,2,3],[4,5,6]])

new = np.delete(a,0,axis=0)
print(new)

'''
[[4 5 6]]

'''