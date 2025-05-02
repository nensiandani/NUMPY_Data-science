import numpy as np

prices = np.array([100,300,450,600])

discount = 10 # scalar single vlaues

final_price = prices - (prices * discount/100)

print(final_price)

'''
[ 90. 270. 405. 540.]

'''