
def withdraw_money(balance,transaction):
  amount=int(input("Enter the amount you want to withdraw :₹"))
  if amount>balance:
    print("Not Enough balance!")
  else:
    balance=balance-amount
    print("₹",amount,"withdrawn successfully!")
    transaction.append("Withdrawn :₹"+str(amount))
  return balance,transaction