# Leap year is divisible by 4, but not 100 unless it is also divisible by 400.

year = 2024
# (year % 4 == 0)
# (year % 100 != 0)
# (year % 400 == 0)

if (year % 400 == 0) and (year % 100 != 0) or (year % 4 == 0):
    print("Leap year")
else:
    print("Not a leap year")
