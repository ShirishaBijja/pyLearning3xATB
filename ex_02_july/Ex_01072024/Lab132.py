# Multiple
class Father:
    def father_money(self):
        return "5"

class Mother:
    def mother_money(self):
        return "2"

    def home(self):
        return "This is from the Mother"


class Son(Mother, Father):
    pass

# Problem - Diamond Problem
# mother first as she called first

son = Son()
son.father_money()
son.mother_money()
print(son.home())  # Method resolution