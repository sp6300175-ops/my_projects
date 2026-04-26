
from display import display_balance
from withdraw import withdraw_money
from deposit import deposit_money
from statement import statement



balance=5000
transaction=[]

def atm():
    global balance, transaction
    while True:
        print("--- ATM MENU ---")
        print("\n\nPress 1 : Display Balance \nPress 2 : Withdraw Money \nPress 3 : Deposit Money \nPress 4 : Statement \nPress 5 : EXIT\n")
        choice=int(input("Enter your choice:"))

        if choice==1:
            display_balance(balance)
        elif choice==2:
            balance,transaction=withdraw_money(balance,transaction)
        elif choice==3:
            balance,transaction=deposit_money(balance,transaction)
        elif choice==4:
            statement(transaction)
        elif choice==5:
            break
        else:
            print("Invalid Input, Enter (1/2/3/4)")
        
if __name__=="__main__":
    atm()