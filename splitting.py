'''  
np.split()

np.vsplit()
np.hsplit()

'''

import numpy as np

a = np.array([1,2,3,4,5,6,7,8])

new = np.split(a,2)
print(new)

'''
[array([1, 2, 3, 4]), array([5, 6, 7, 8])]

'''