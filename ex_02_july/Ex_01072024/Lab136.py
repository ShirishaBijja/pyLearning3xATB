# Polymorphism
# It allows objects of different classes to be treated as objects of a common superclass

# Object -> method -> mother, sister, daughter

# Method Overloading
# Method overriding

class Shape:
    def area(self):
        print("Area of the shape")

class Rectangle(Shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 *self.radius * self.radius

circle = Circle(10)
print(circle.area())