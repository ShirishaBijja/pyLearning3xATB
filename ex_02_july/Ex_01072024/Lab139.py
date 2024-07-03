class MathUtils(object):
    def add(self,a,b=0,c=0):
        return a+b+c

math = MathUtils()
print(math.add(2))
print(math.add(2,4))
print(math.add(2,4,5))