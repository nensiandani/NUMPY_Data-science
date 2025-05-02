
prices = [100,300,700,950]

discount = 10

final_prices = []

for p in prices:
    final_price = p -(p * discount/100)
    final_prices.append(final_price)

print(final_prices)

'''
[90.0, 270.0, 630.0, 855.0]

'''