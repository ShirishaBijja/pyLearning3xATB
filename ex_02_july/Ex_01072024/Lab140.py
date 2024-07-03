# Abstraction

from abc import ABC,  abstractmethod
class Animal(ABC):
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        return "Meow"

cat = Cat()
print(cat.sound())