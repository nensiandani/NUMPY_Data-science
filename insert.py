'''
np.insert(array, index, vlaue , asix=none)
array = original array
insert
vlaue
asix=0  row
asix=1  column

'''


import numpy as np 

a = np.array([10,20,30,40,50,60,70])
print(a)

new_a =np.insert(a,4,80)
print(new_a)

'''
[10 20 30 40 50 60 70]
[10 20 30 40 80 50 60 70]

'''