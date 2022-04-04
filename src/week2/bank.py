print("Welcome to our banking system!")


balance = 0
print("Initial Balance: " + str(balance))
def withdraw (amount):
  global balance
  if int(amount) > balance:
    print("Impossible. Your withdrawal is higher than your current balance.")
  else:
    balance = balance -int(amount)
    print (balance)
  
def deposit (amount):
  global balance
  balance = balance+int(amount)
  print (balance)
  


while True:
  action = input("Type 1 to withdraw money. Type 2 to deposit money. Type 3 to check balance. Type 4 to exit. ")
  if action == '1':
    amount = input("How much money will you withdraw? ")
    withdraw(amount)
  elif action == '2':
     amount = input("How much money will you deposit? ")
     deposit(amount)
  elif action == '3':
    print (balance)
  elif action == '4':
    break
  else:
    print ("Invalid Number. Try Again.")

