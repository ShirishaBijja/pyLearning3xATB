# incomplete
class BankAccount:

    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def __withdraw(self, amount):
        self.balance -= amount

    def __show_balance(self):
        print("Ypur balance is ", self.balance)

    def if_you_are_auth(self,flag):
        if flag:
            self.__show_balance()
        else:
            print("Not allowed")

    def if_you_auth_user(self, auth, amount):
        if auth:
            self.__withdraw(amount=amount)
        else:
            print("Not allowed")



jp_chase = BankAccount()
jp_chase.deposit(100)
jp_chase.if_you_are_auth(False)
jp_chase.if_you_auth_user(True, 99)

secret_pass = input("Enter the pin")
if secret_pass == "1234":
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth(False)

secret_pass = input("Enter your Pin to withdraw")
your_amount = int(input("Enter your amount to withdraw"))


