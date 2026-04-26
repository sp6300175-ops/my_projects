import random
def rock_paper_scissor():
  
  print("\n\n------Rock 🪨  Paper 📃  Scissor ✂️  Game------")
  user_choice=input("\nChoose Rock, Paper or Scissor:").strip().lower()
  lst=["rock","paper","scissor"]
  if user_choice in lst:
    ch1=random.choice(lst)
    if user_choice==ch1:
      print("It's a Draw🤝")
      print("You:",user_choice,"Computer:",ch1)
    elif (user_choice=='rock' and ch1=='scissor') or (user_choice=='scissor' and ch1=='paper') or(user_choice=='paper' and ch1=='rock'):
      print("You Win!!🥳")
      print("You:",user_choice,"Computer:",ch1)
    else:
      print("You Lose! Better luck next time")
      print("You:",user_choice,"Computer:",ch1)
  else:
    print("Invalid Input, Enter (rock/paper/scissor)")