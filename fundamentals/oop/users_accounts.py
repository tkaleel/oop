class BankAccount:
    accounts = []
    def __init__(self, interest_rate, account_balance=0):
        self.interest_rate = interest_rate
        self.account_balance = account_balance
        BankAccount.accounts.append(self)
            
    def make_deposit(self, amount):	
        self.account_balance += amount
        return self	

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print("Balance: $", self.account_balance)

    def yield_interest(self):
        self.account_balance = self.account_balance+(self.account_balance*self.interest_rate)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_user_balance()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(interest_rate=0.02, account_balance=0)
    
    def make_deposit(self, amount):	
        self.account.account_balance += amount
        return self	

    def make_withdrawal(self, amount):
        self.account.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print("User:",self.name+", Balance:",self.account.account_balance)

theo = User("Theo", "theo@python.com")
steve = User("Steve", "steve@python.com")
sachiko = User("Sachiko", "princess_sachiko@dogmail.com")

sachiko.make_deposit(100000).display_user_balance()
