# Leap year checker

year = int(input("Enter the year\n"))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))


# Triangle Classifier:

side1 = int(input("Enter side1 of the triangle"))
side2 = int(input("Enter side2 of the triangle"))
side3 = int(input("Enter side3 of the triangle"))

if side1 == side2 and side1 == side3:
    print("Equatorial triangle")
elif side1 > side2 and side1 > side3:  #side1 is greater than both
    if side2 > side3 or side3 > side2:
        print("Scalene")
    else:
        print("Isosceles Triangle")
elif side2 > side1 and side2 > side3:
    if side1 > side3 or side3 > side1:
        print("Scalene")
    else:
        print("Isosceles Triangle")
elif side3 > side1 and side3 > side2:
    if side1 > side2 or side2 > side1:
        print("Scalene")
    else:
        print("Isosceles Triangle")


# Fibonacci series

num = int(input("Enter the number\n"))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()


# Factorial
num = 5
factorial = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
