initially=100000
bank=100000
win=100*0.6
lose=100*0.4
for i in range(int(win)):
    bank=(bank/100)*110
for i in range(int(lose)):
    bank=(bank/100)*90

if bank>initially:
    print("Do it")
else:
    print("Nope!!!")