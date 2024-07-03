# Method Overloading - is not supported in Python

class MathUtils(object):
    def add(self,a,b):
        return a+b

    def add(self,a,c):
        return a-c

math = MathUtils()
print(math.add(2,4))  # lastone it is talking, if we have same name