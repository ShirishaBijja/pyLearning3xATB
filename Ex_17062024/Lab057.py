# Functions
# block of Code - which can exected or reused.
# Define
# Call

# Built functions - builtins.py - file (Python 3 setup)
# which are created by the Python Contributers
result = max(2, 3)

# User defined
# They can return something
# They can't return -> non return
# They have parameters
# They don't have

def say_hello():   # No return type and without argument/parameter.
    print("hello")

say_hello()

def say_hello_arg(name):  # No return type and with argument
    print("Hello", name)

say_hello_arg("Pramod")
say_hello_arg("amit")


def say_hello_arg_default(name = "Pramod"):  # No return type with default value
    print("Hello", name)

say_hello_arg_default()
say_hello_arg_default("Deeksha")
say_hello_arg_default(name="sachin")

def sum_number_argument_ret(a, b):  # Argument + return Type
    return a+b

result1 = sum_number_argument_ret(3,4)
result = sum_number_argument_ret(a = 90, b = 5)
print(result)