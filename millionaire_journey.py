#How many months will it take to be a Millionaire



def investment_func():
    is_running=True
    while is_running:
        try:
            x = int(input("How much is your initial investment? : $"))
        except ValueError:
            print("Invalid input!!!")
        else:
            is_running = False
            return x
def rate_func():
    is_running = True
    while is_running:
        try:
            r = int(input("Expected annual interest rate : ")) / 12
        except ValueError:
            print("Invalid input!!!")
        else:
            is_running=False
            return r
def cont_func():
    is_running = True
    while is_running:
        try:
            c = int(input("How much is your monthly contribution? : $"))
        except ValueError:
            print("Invalid input!!!")
        else:
            is_running=False
            return c







initial=investment_func()
investment=initial
rate=rate_func()
cont=cont_func()
months=0


while investment<1000000:
    months+=1
    investment+=investment*(rate/100)
    investment+=cont

print()
print(f"It takes {months//12} years and {months%12} months to be Millionaire")
print()
print(f"Your initial investment : {initial+(cont*(months-1))}\nYour gain : {investment-(initial+(cont*(months-1)))}")
