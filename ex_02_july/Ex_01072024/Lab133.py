class A:
    def methodA(self):
        return "method A"


class B:
    def methodB(self):
        return "method B"

class C(B,A):
    pass

c = C()
print(c.methodB())
print(c.methodA())
