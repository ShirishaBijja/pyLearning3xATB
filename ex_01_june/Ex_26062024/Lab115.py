class Dog:
    name = None
    id = None

    def __init__(self):
        print("Default - No argument")
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def sleep(self):
        print("who is Sleeping -> " + self.name)

# line 5 and 9 are methods
# instance variable - 2 and 3 lines
# line 5 is constructor. Constructor doesn't have return variable


dog1 = Dog("Chow", "1")
dog2 = Dog("Mow", "2")


print(f'{dog1.name} has ID {dog1.id}')
print(f'{dog2.name} has ID {dog2.id}')

dog1.sleep()