class Car:
    name = None

    def __init__(self):
        self.public_var = "public"
        self.protected_var = "protected123"
        self.__private_var = "pass@123"

    def __private_method(self):
        print("Protected")

    def printName(self):
        if self.__private_var == "123":
            print("Hi, 123")
        print("I am allowed public")

# This is the end of the class

alto = Car()
alto.public_var = "Hahaha"
