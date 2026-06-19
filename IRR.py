def cashflows():
    cashlist=[]
    while True:
        try:
            years=int(input("How many years of cash flows do you have including year 0 : "))
        except ValueError:
            print("Enter only integers!")
        else:
            if years>0:
                for i in range(years):
                    while True:
                        try:
                            cf=float(input(f"Year {i} cash flow : "))
                            cashlist.append(cf)
                            break
                        except ValueError:
                            print("Enter only integers!")
            else:
                print("Enter only positive numbers!")
                continue
            break
    return cashlist

def npv():
    while True:
        try:
            df = float(input("Input discount factor : ")) / 100
            break
        except ValueError:
            print("Enter only integers!")
    cash=cashflows()
    netpv=cash[0]
    for i in range(1,len(cash)):
        netpv+=cash[i]/(1+df)**i
    return netpv,df


print("When asking rate please enter lower rate first!")
netpv1,df1=npv()
netpv2,df2=npv()

print(f"IRR : {(df1+(netpv1/(netpv1-netpv2)*(df2-df1)))*100:.2f}%")