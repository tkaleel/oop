class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    # adding the deposit method
    def make_deposit(self, amount):	
    	self.account_balance += amount	

    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print("User:",self.name+", Balance:",self.account_balance)
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

theo = User("Theo", "theo@python.com")
steve = User("Steve", "steve@python.com")
sachiko = User("Sachiko", "princess_sachiko@dogmail.com")

theo.make_deposit(100)
theo.make_deposit(100)
theo.make_deposit(100)
theo.make_withdrawal(50)
theo.display_user_balance()

steve.make_deposit(500)
steve.make_deposit(500)
steve.make_deposit(500)
steve.make_withdrawal(500)
steve.display_user_balance()

sachiko.make_deposit(100000)
sachiko.make_withdrawal(1)
sachiko.make_withdrawal(1)
sachiko.make_withdrawal(1)
sachiko.display_user_balance()

theo.transfer_money(sachiko, 250)
theo.display_user_balance()
sachiko.display_user_balance()