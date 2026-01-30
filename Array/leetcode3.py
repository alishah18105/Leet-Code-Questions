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

    
