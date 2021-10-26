class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    # adding the deposit method
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self	

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print("User:",self.name+", Balance:",self.account_balance)
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self, other_user

theo = User("Theo", "theo@python.com")
steve = User("Steve", "steve@python.com")
sachiko = User("Sachiko", "princess_sachiko@dogmail.com")

theo.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(50).display_user_balance()

steve.make_deposit(500).make_deposit(500).make_deposit(500).make_withdrawal(500).display_user_balance()

sachiko.make_deposit(100000).make_withdrawal(1).make_withdrawal(1).make_withdrawal(1).display_user_balance()

theo.transfer_money(sachiko, 250)
theo.display_user_balance()
sachiko.display_user_balance()