class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(balance = 0)
    def make_deposit(self):
        self.account.deposit(100)
        return self
    def make_withdraw(self):
        self.account.withdraw(100)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self

class BankAccount:

    all_accounts = []
    def __init__(self, balance = 0):
        self.balance = balance
        BankAccount.all_accounts.append(self)

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

luis = User("Luis","luis@gmail")
grace = User("Grace", "grace@gmail")

print(luis.name)
luis.make_deposit().make_deposit().make_deposit().make_withdraw().display_user_balance()
