# Triangle classifier

side1 = int(input("Enter side1"))
side2 = int(input("Enter side2"))
side3 = int(input("Enter side3"))

if side1 == side2 == side3:
    print("Equitorial triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Iso triangle")
else:
    print("scalene")

