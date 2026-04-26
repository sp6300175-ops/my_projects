import random
def dice_roll():
  
  print("\n\n------Dice Roll Game🎲------")
  user_choice1=int(input("\nGuess dice number of your choice (1/2/3/4/5/6):\n"))
  ch1=random.randint(1,6)
  if user_choice1 in [1,2,3,4,5,6]:
    if user_choice1==ch1:
      print("BINGO!! YOU GUESSED IT RIGHT.🎲🔥")
      print("Your choice:",user_choice1,"Computer:",ch1)
    else:
      print("OOPS! The dice rolled",ch1,"Try Again!")
      print("Your choice:",user_choice1,"Computer:",ch1)
  else:
    print("Invalid Input! Choose(1/2/3/4/5/6)")