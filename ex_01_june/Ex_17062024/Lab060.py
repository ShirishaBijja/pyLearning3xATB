#  *args  - any number of arguments
print("Pramod", "Amit", "SB")


def sum3(a=1, b=1, c=1):
    return a + b + c


# result = sum3()  # o/p: 3
# result = sum3(2, 3, 4)  # o/p:9
# result = sum3(a=3)  #o/p: 5
result = sum3(a=3, b=8)  #o/p:12
print(result)
