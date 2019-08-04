class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter
        # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_widtharwal(self,amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"{self.name} {self.account_balance}")
    def transfer_money(self, other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"{self.name} {self.account_balance}")
        print(f"{other_user.name} {other_user.account_balance}")


eric = User("ecfang","ericfang@123.com")
elisa = User("elisa", "elisa@123.com")
bob = User("bobby", "bobby@123.com")
eric.make_deposit(100)
eric.display_user_balance()
eric.make_deposit(100)
eric.display_user_balance()
eric.make_deposit(100)
eric.display_user_balance()
eric.make_widtharwal(50)
eric.display_user_balance()
elisa.make_deposit(100)
elisa.display_user_balance()
elisa.make_deposit(100)
elisa.display_user_balance()
elisa.make_widtharwal(50)
elisa.display_user_balance()
elisa.make_widtharwal(20)
elisa.display_user_balance()
bob.make_deposit(500)
bob.display_user_balance()
bob.make_widtharwal(50)
bob.display_user_balance()
bob.make_widtharwal(50)
bob.display_user_balance()
bob.make_widtharwal(50)
bob.display_user_balance()

eric.transfer_money(elisa,50)

