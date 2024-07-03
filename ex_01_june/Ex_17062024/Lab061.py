def print_argument(*args):   # ["pramod", "amit", "lucky"]
    for i in args:
        print(i, end = " ")


print_argument("pramod", "amit", "lucky")

# *args -> List
a = ["pramod", "amit", "lucky"]
for i in a:
    print(i)