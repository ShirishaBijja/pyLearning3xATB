class BankAccount:

    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print("Ypur balance is ", self.balance)

jp_chase = BankAccount()
print(jp_chase.balance)
jp_chase.deposit(101)
jp_chase.show_balance()
jp_chase.deposit(99)
jp_chase.show_balance()
jp_chase.withdraw(199)  # bad function, anyone cant withdraw
jp_chase.show_balance()