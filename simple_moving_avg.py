prices_list=[10,20,30,40,50]
window_size=3

def simple_moving_avg(prices,k):
    count=0
    avg=[]
    for i in range((len(prices) - k) + 1):
        window=prices[i:i+k]
        avg.append(sum(window)/len(window))
    for x in range(len(avg)-1):
       if avg[x+1]>avg[x]:
           count+=1
       else:
           count-=1
    if count>0:
        return "There is an uptrend"
    elif count==0:
        return "It is a mix market"
    else:
        return "There is a downtrend"


print(simple_moving_avg(prices_list,window_size))
