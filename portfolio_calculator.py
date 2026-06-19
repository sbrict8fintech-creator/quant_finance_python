import random

def daily_return(x):
    returns=[]
    for i in range(len(x)-1):
        returns.append((((x[i+1])-x[i])/x[i]))
    return returns

def mean(x):
    means=0
    for num in x:
        means+=num
    return means/len(x)

def variance(x):
    average=mean(x)
    sq_root=0
    for num in x:
        sq_root+=(num-average)**2
    return sq_root/len(x)

def std_dv(x):
    var=variance(x)
    return var**0.5

def covariance(x,y):
    return_a=daily_return(x)
    return_b=daily_return(y)
    average_a=mean(return_a)
    average_b=mean(return_b)
    deviation_a=[]
    deviation_b=[]
    for i in range(len(return_a)):
        deviation_a.append(return_a[i]-average_a)
    for i in range(len(return_b)):
        deviation_b.append(return_b[i] - average_b)
    total=0
    for i in range(len(deviation_a)):
        total+=deviation_a[i]*deviation_b[i]
    return total/len(deviation_a)

def covariance_matrix(x):
    matrix=[]
    store=[]
    for i in range(len(x)):
        for j in range(len(x)):
            store.append(covariance(x[i],x[j]))
        matrix.append(store)
        store=[]
    return matrix

def portfolio_return(x,y):
    expected_return=0
    for i in range (len(x)):
        expected_return+=x[i]*y[i]
    return expected_return

def portfolio_variance(x,y):
    total=0
    for i in range(len(x)):
        for j in range(len(x)):
            total+=(x[i]*x[j])*(y[i][j])
    return total

def portfolio_variance2(s,w):
    returns=[]
    portfolio_return_=[]
    for i in range (len(s)):
        returns.append(daily_return(s[i]))
    total=0
    for i in range(len(w)):
        for j in range(len(w)):
            total+=w[j]*returns[j][i]
        portfolio_return_.append(total)
        total=0
    variance2=variance(portfolio_return_)
    return variance2

def sharp_ratio(pv,pr):
    free_rate=2/100
    return (pr-free_rate)/pv**0.5

def random_weight(n):
    r_weights=[random.random() for i in range(n)]
    total=sum(r_weights)
    new_weights=[j/total for j in r_weights]
    return new_weights

def efficient_frontier(n,len_w):
    mean_return2=mean_return
    return_std=[]
    for i in range (n):
        storage=[]
        new_weights2=random_weight(len_w)
        total=0
        for j in range(len(new_weights2)):
            total+=mean_return2[j]*new_weights2[j]
        storage.append(total)
        var2=portfolio_variance2(stocks,new_weights2)
        storage.append(var2**0.5)
        return_std.append(storage)
    return return_std

def best_sharp(n,len_w):
    free_rate=2/100
    eff_frontier_list=efficient_frontier(n,len_w)
    highest=0
    best_option=[]
    for i in range (n):
        for j in range (len(eff_frontier_list[i])-1):
            current=(eff_frontier_list[i][j]-free_rate)/eff_frontier_list[i][j+1]
            if current>highest:
                highest=current
                best_option=[eff_frontier_list[i][j],eff_frontier_list[i][j+1]]
            else:
                continue
    best_option.append(highest)
    return best_option

a=[100,200,250,375]
b=[25,40,50,90]
c=[200,180,198,210]

stocks=[a,b,c]

weights = [0.4, 0.35, 0.25]
mean_return=[mean(daily_return(a)),mean(daily_return(b)),mean(daily_return(c))]

print(best_sharp(1000,len(weights)))

