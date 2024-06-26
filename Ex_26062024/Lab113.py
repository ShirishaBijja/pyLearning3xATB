# Class - is just a blueprint to create an object.
# When class is created no memory allocation is taken
# When an Object is created, it takes memory allocation

class Person:
    # Attributes
    name = None
    id = None
    age = None
    phone_number = None

    # Behaviour
    def talk(self):  # No arg, No return
        print("I can talk")

    def sleep(self, name):  # 1 Arg, No return
        print("I am a method")
        print("Sleep", name)

    def sleep1(self, name):  # 1 Arg with return
        print("I am a method")
        return None

    def walk(self):
        print("I am Walking")

    def walk_return(self):   # No Arg with Return
        return "I am walking"

# Create Object of the Person Class
# ObjectRef = Object -> ClassName()
surya = Person()
surya.name = "Surya Prakash"
surya.talk()

rithika = Person()
rithika.name = "Rithika Gupta"
rithika.walk()

# Both objects havs different memory allocation