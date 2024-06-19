# Tuple - Collection of Items

my_list = [1, 2, 3]
print(id(my_list))
my_list[0] = 21
print(my_list)
print(id(my_list))

# O/P:
# 1572318794112
# [21, 2, 3]
# 1572318794112

my_tuple = (1,2,3,4,5,5,4)
# my_tuple[0] = 21  # immutable can't change
print(my_tuple)