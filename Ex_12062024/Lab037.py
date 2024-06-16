# Conditions and loop
# ++ and -- does not exists in python

# age > 18 -> You are allowed to go the club
# age < 18 -> You are not allowed

# If, Else
# Syntax
# if condition:
#    code to be executed
# else:
#     code to be executed when condition is false

# Write a program to take a user age and let him know if he can go the club.

# take a user input

age = int(input("Enter the age:"))

if age > 18:
    print("Go to the club")
else:
    print("Not allowed")