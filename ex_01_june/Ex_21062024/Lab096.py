# Decorators
# A decorator is essentially a func that takes another func as argument
# returns a new func that usually extends

def my_decorator(func):
    def wrapper():
        print("Starting....")
        print("***********")
        func()
        print("****")
        print("Ending")

    return wrapper()

@my_decorator
def say_hello():
     print("Say hello")


# Output:
# Starting....
# ***********
# Say hello
# ****
# Ending