# Multiple and Multi level

class A:
    def methodA(self):
        return "method A"


class B(A):
    def methodB(self):
        return "method B"

class C(A):
    def methodC(self):
        return "method C"

class D(C,B):
    pass