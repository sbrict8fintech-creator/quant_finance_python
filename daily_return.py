prices=[100,105,102]

def daily_returns(prices):
    changes = []
    for i in range(len(prices)-1):
        changes.append(((prices[i+1]-prices[i])/prices[i])*100)
    return changes


print(daily_returns(prices))