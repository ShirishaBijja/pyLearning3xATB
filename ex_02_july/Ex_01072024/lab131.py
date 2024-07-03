# Multi level Inheritance
class Grandparent:
    def grandparent_method(self):
        return "Grandparent's method"

class Parent(Grandparent):

    def parent(self):
        return "Parent's method"

class Child(Parent):
    mac_m3_apple = "M3 Max"
    def child(self):
        return "Child's method"

child = Child()
print(child.grandparent_method())