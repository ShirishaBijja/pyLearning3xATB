# Map - return numbers

numbers = [ 1,2,3,3,4,4,5,5,6]
def double_me(num):
    return num * 2

new_list_double = map(double_me, numbers)
print(list(new_list_double))

# Lambda
double_me_lambda = lambda n: n*2


# Filters - functions true or false
# pick item m is true keep it, false - remove it
# it can give less number of items as compared to actual list

def even_giver(num):
    return num%2==0

# new_filtered_list = list(filter(even_giver, numbers))
new_filtered_list = list(filter(lambda n: n%2 == 0, numbers))
print(new_filtered_list)