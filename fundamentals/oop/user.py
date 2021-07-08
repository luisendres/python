class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdraw(self, amount):
        self.balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name} \nAccount Balance: ${self.balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        print(f"User: {self.name} \nAccount Balance: ${self.balance}")
        print(f"User: {other_user.name} \nAccount Balance: ${other_user.balance}")
        return self

luis = User("Luis", 2000)
grace = User("Grace", 100000)
nina = User("Nina", 50000)

luis.make_deposit(1000).make_deposit(1000).make_deposit(2000).make_withdraw(3000).display_user_balance().transfer_money(grace, 1000)

grace.make_deposit(1000).make_deposit(1000).make_withdraw(100).make_withdraw(100).display_user_balance()

nina.make_deposit(2000).make_withdraw(1000).make_withdraw(1000).display_user_balance()

luis.transfer_money(nina, 1000)