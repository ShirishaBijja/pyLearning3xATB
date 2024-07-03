from abc import ABC,  abstractmethod

class PyATB(ABC):

    def payFee(self):
        pass

    def enrolled(self):
        print("Enrolled")

class Shubham(PyATB):
    def payFee(self):
        print("paid")


subham = Shubham()
print(subham.enrolled())