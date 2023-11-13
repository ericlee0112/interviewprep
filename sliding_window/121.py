import math
# best time to buy and sell stock
'''
   *
[7,1,5,3,6,4]

keep track of min 


min = 1
profit = 0


'''

def maxProfit(prices):
    max_profit = 0
    min_so_far = math.inf

    # loop through prices
    for price in prices:
        min_so_far = min(min_so_far, price)
        max_profit = max(max_profit, price - min_so_far)
    
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
