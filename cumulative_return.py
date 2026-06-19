monthly_return=[3,-1.5,2,4,-0.8]
def cumulative_return(returns):
    capital=100
    for rate in returns:
        capital=(capital*(100+rate))/100
    gain=capital-100
    return f"{gain:.2f}%"


print(cumulative_return(monthly_return))
