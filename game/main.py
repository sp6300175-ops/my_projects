from rock_paper_scissor import rock_paper_scissor
from dice_roll import dice_roll


def game():
    while True:
        print("\n\n---~   MENU    ~---")
        print("\n1.Stone-Paper-Scissors \n2.Dice Roll Game\n--TO EXIT PRESS 3--\n")
        choice=int(input("Enter your choice :"))
        if choice==1:
            rock_paper_scissor()
        elif choice==2:
            dice_roll()
        elif choice==3:
            break
        else:
            print("Invalid Input!! choose(1/2/3)")

if __name__=="__main__":
    game()