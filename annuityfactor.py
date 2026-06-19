def annuity_factor():
    while True:
        try:
            rate=float(input("Input the rate : "))/100
            break
        except ValueError:
            print("Input integers/floats only!")
    while True:
        try:
            year=int(input("What year annuity factor : "))
            break
        except ValueError:
            print("Input integers only!")
    nominator=1
    denominator=(1+rate)**year
    for i in range(year-1):
        nominator+=(rate+1)**(i+1)


    return nominator/denominator

print(f"{annuity_factor():.3f}")