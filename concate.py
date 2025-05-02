'''
np.concatenate((arra1,arr2), axis=0)
axis=0 vertical
axis=1 horizontal

'''

import numpy as np

a1= np.array([1,2,3])
a2= np.array([4,5,6])

new = np.concatenate((a1,a2))
print(new)

'''
[1 2 3 4 5 6]

'''