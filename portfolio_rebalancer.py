is_running=True


while is_running:
    try:
        fund=int(input("How much do we have to invest? : $"))
    except ValueError:
        print("Invalid input!!!")
    else:
        stocks=round(fund*0.6,2)
        bonds=round(fund*0.4,2)
        print(f"We have : ${fund}\nStocks : ${stocks}\nBonds : ${bonds}")
        is_running=False


is_running=True
while is_running:
    try:
        cur_val_stocks=int(input("What is the current value of your stock holdings? : $"))
    except ValueError:
        print("Invalid input!!!")
    else:
        yes=True
        while yes:
            try:
                cur_val_bonds=int(input("What is the current value of your bond holdings? : $"))
            except ValueError:
                print("Invalid input!!!")
            else:
                current_value=cur_val_stocks+cur_val_bonds
                print(f"Current value of your portfolio is ${current_value}")
                yes=False
                is_running=False

difference_stocks=cur_val_stocks-(current_value*0.6)
if difference_stocks>0:
    print(f"Sold ${difference_stocks} worth shares!!!")
    cur_val_stocks-=difference_stocks
else:
    print(f"Bought ${difference_stocks-(difference_stocks*2)} worth shares!!!")
    cur_val_stocks+=(difference_stocks-(difference_stocks*2))

difference_bonds=cur_val_bonds-(current_value*0.4)
if difference_bonds>0:
    print(f"Sold ${difference_bonds} worth bonds!!!")
    cur_val_bonds-=difference_bonds
else:
    print(f"Bought ${difference_bonds-(difference_bonds*2)} worth bonds!!!")
    cur_val_bonds+=(difference_bonds-(difference_bonds*2))

print()
print(f"Rebalanced value of stocks : ${cur_val_stocks}")
print(f"Rebalanced value of bonds : ${cur_val_bonds}")