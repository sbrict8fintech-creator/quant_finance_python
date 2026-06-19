investment=int(input("Your initial investment : "))
cont=int(input("Your monthly contribution : "))
years=int(input("For how many years : "))
rate=8/365
month=1
while month<=years*12:
    for i in range (30):
        investment*=(100+rate)/100
    print(f"Month {month} : {investment:.2f}")
    contribution=cont
    investment+=contribution
    month+=1
