class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def make_deposit(self, amount):
        self.balance += amount
    def make_withdraw(self, amount):
        self.balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name} \nAccount Balance: ${self.balance}")
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        print(f"User: {self.name} \nAccount Balance: ${self.balance}")
        print(f"User: {other_user.name} \nAccount Balance: ${other_user.balance}")

luis = User("Luis", 1000)
grace = User("Grace", 100000)
nina = User("Nina", 50000)

luis.make_deposit(1000)
luis.make_deposit(1000)
luis.make_deposit(2000)
luis.make_withdraw(3000)
luis.display_user_balance()

grace.make_deposit(1000)
grace.make_deposit(1000)
grace.make_withdraw(100)
grace.make_withdraw(100)
grace.display_user_balance()

nina.make_deposit(2000)
nina.make_withdraw(1000)
nina.make_withdraw(1000)
nina.display_user_balance()

luis.transfer_money(nina, 1000)