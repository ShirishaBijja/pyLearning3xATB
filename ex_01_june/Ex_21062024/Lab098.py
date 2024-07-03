import time


def decorator1(func):
    def wrapper():
        func()
        print("decor1")
    return wrapper


def decorator2(func):
    def wrapper():
        func()
        print("decor2..")
    return wrapper

@decorator1
@decorator2
def say_func():
    print("Hello")

say_func()