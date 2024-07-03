# Method Overriding - same name in parent and child
# Child always overrid the parent functions
# Super means call my parent functions

class Father:
    def home(self):
        print("1BHK")

class Son(Father):
    def home(self):
        super().home()  # Parent class
        print("3BHK")

pramod = Son()
pramod.home()