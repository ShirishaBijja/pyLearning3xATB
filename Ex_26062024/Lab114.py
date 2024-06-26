class Dog:
    name = None
    id = None

    def __init__(self, name, id):
        self.name = name
        self.id = id

    # Constructor ?
    # Use to initialize the values
    # of the instance variables (Attributes)
    # two types of Constructor - default and parameterised

    def sleep(self):
        print("Sleeping")


dog1 = Dog()
dog1.name = "Chow"
print(dog1.name)   # Chow
dog1.sleep()       # Sleeping

dog2 = Dog()
print(dog2.name)    # None
dog2.name = "Mow"
print(dog2.name)    # Mow
