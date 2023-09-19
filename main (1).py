class BankAccount:
  def __init__ (self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name=account_holder_name
    self.__account_balance=initial_balance
  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited {}. New balance {}".format(amount,self.__account_balance))
    else:
      print("Invalid deposit amount.")
  def withdraw(self, amount):
    if amount > 0 and amount <=self.__account_balance:
      self.__account_balance = self.__account_balance - amount
      print("Withdrew *{}. New balance: *{}".format(amount,self.__account_balance))
    else:
      print("Invalid withdrawal amount or insufficient balance.")
  def balance (self):
    print("Account balance for {} (Account #{}): *{}".format( self.__account_holder_name,self.__account_number, self.__account_balance))
holder= input("Enter the account holder name: ")
number=int(input("Enter the account number: "))
account = BankAccount(account_number=number,
account_holder_name=holder,initial_balance=5000.0)
account.balance ()
account.deposit (500.0)
account.withdraw(200.0)
account.balance()