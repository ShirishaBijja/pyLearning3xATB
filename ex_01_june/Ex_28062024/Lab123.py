# Encapsulation - bind the data variables with the methods
# Data Member - / Class Variables
# Methods - Def function within the class
# wrapping or binding the data variables with the methods - Encapsulation

# Hide the data members(class variables, instance variables) by using only the methods

class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when an object is created")

# password can only changed using change function but not outside
    def change_password(self):
        self.password = "345"
# This is end of the class

xuv = Car()
xuv.password = "345"