import numpy as np

a= np.array([[1,2],[3,4]])
print(a)

b = np.insert(a,1,[5,6], axis=0)
print(b)

'''
[[1 2]
 [3 4]]
[[1 2]
 [5 6]
 [3 4]]
 '''