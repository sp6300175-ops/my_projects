
def deposit_money(balance,transaction):
  amount=int(input("Enter the amount you want to deposit :₹"))
  balance=balance+amount
  print("₹",amount,"deposited successfully!")
  transaction.append("deposited :₹"+str(amount))
  return balance,transaction