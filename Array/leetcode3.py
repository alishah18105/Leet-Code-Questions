#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

prices = [7,1,5,3,6,4]
buy = prices[0] 
sell = prices[1] 
profit = 0

for i in range(1, len(prices)-1,1):
    if buy < prices[i]:
        if sell < prices[i+1]:
            sell = prices[i+1] 
    else:
        buy = prices[i]
        sell = prices[i+1]

if buy < sell:
    profit = sell - buy
else:
    profit = 0
print(buy,sell, profit)

    
