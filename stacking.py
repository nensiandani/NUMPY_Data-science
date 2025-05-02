'''
vertical
horizontal

'''

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.vstack((a,b)))  # vertical
print(np.hstack((a,b)))  #horizontal

'''
[[1 2 3]
 [4 5 6]]
[1 2 3 4 5 6]

'''