import numpy as np 

a = np.array([10,20,30,40,50,60])

print(a[0:5])
print(a[:4])
print(a[::2])
print(a[::-1])

'''
[10 20 30 40 50]
[10 20 30 40]
[10 30 50]
[60 50 40 30 20 10]

'''