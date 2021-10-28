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

steve = BankAccount(.01)
sachiko = BankAccount(.01, 500)

steve.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(100).yield_interest().display_user_balance()

sachiko.make_deposit(1000).make_deposit(1000).make_withdrawal(1).make_withdrawal(1).make_withdrawal(1).make_withdrawal(1).yield_interest().display_user_balance()

BankAccount.print_all_accounts()