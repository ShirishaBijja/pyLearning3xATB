# Program - Calculate the area of Circle
# input -> radius
# output -> area
import math

# data types
# input -> int or float -> float
# output -> float

# Core logic -> pi*r*r

radius = float(input("enter the radius\n"))
print(math.pi)
area = math.pi*(radius ** 2)
area2 = math.pi*(math.pow(radius, 2))
print(area)
print(area2)


