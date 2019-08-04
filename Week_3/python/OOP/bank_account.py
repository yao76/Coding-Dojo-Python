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


eric = BankAccount(0,0)
bob = BankAccount(.02,100)
eric.deposit(10).deposit(10).deposit(10).withdraw(20).yield_interest()
bob.deposit(10).deposit(10).deposit(10).withdraw(20).yield_interest()
eric.display_account_info()
bob.display_account_info()
