class BankAccount:
# don't forget to add some default values for these parameters!
    all_accounts = []
    def __init__(self,int_rate = .01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
# your code here! (remember, instance attributes go here)
# don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Account Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if BankAccount.is_positive(self.balance):
            temp = self.balance * self.int_rate
            self.balance += temp
        # print(f"Interest: ${temp}")
        # print(f"Interest: ${self.balance}")
        return self

    @staticmethod
    def is_positive(balance):
        if(balance < 0):
            return False
        else:
            return True

    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

    @classmethod
    def all_info(cls):
        for BankAccount in cls.all_accounts:
            print(BankAccount.balance)

luis = BankAccount(balance = 100)
grace = BankAccount(balance = 1000)

luis.deposit(10).deposit(10).deposit(10).withdraw(300).yield_interest().display_account_info()
grace.deposit(100).deposit(100).withdraw(10).withdraw(10).withdraw(10).withdraw(10).yield_interest().display_account_info()

BankAccount.all_info()

