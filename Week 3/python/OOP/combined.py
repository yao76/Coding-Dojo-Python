class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account = BankAccount(int_rate=0.02, balance=0)		# the account balance is set to $0, so no need for a third parameter
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    def make_widtharwal(self,amount):
        self.account.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"{self.name} {self.account.account_balance}")
        return self
    def transfer_money(self, other_user,amount):
        self.account.account_balance -= amount
        other_user.account.account_balance += amount
        print(f"{self.name} {self.account.account_balance}")
        print(f"{other_user.name} {other_user.account.account_balance}")
        return self

class BankAccount:
    def __init__(self, int_rate = .01, balance = 0):
        self.interest = int_rate
        self.account_balance = balance
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        if(self.account_balance - amount < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        else:
            self.account_balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.account_balance}")
        print(f"Interest: {self.interest}")
        return self
    def yield_interest(self):
        if(self.account_balance > 0):
            self.account_balance = self.account_balance + self.account_balance*self.interest
        else:
            print("Negative account balance")
        return self

eric = User("eric", "eric@123.com")
eric.account.deposit(500)
print(eric.account.interest)
print(eric.account.account_balance)