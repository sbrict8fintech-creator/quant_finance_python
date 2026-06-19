prices=[7,1,5,3,6,4,100]

profit=0
buy_list=[]
sell_list=[]
for price in prices:
    buy=0-price
    position=prices.index(price)
    for i in range(position+1,len(prices)):
        this_profit=buy+prices[i]
        if this_profit>profit:
            profit=this_profit
            buy_list.append(price)
            sell_list.append(prices[i])
        else:continue

for i in range(len(buy_list)):
    check=(0-buy_list[i])+sell_list[i]
    if profit==check:
        print(f"Buy at {buy_list[i]} and sell at {sell_list[i]}")


