# Develop a Python script that calculate the sqaure and cube of a given number. num = 2, sq = 4, c= 8

num = 2
square = num ** 2
cube = num ** 3
print("Num is: ", num)
print("Square of num: ", square)
print("Cube of the num: ", cube)


# Create a program that takes two numbers as input and prints whether the first number is greater then, less than, or equal to the second number.
num1 = int(input("Enter the first number:\t"))
num2 = int(input("\nEnter the second number:\t"))
if num1 > num2:
    print("Number1 is greater than Number2")
elif num2 > num1:
    print("Number2 is greater than Number1")
else:
    print("Both are equal")