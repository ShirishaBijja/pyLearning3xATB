class Calc:

    def __init__(self):
        print("Hello Default constructor")
    def sum(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b

    def div(self, a,b):
        return a/b

object_ref = Calc()
output = object_ref.sum(1,3)
print(output)