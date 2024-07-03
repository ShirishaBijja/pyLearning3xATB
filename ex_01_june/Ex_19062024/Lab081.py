my_l =[1,2,3,4,5]
def double_item(num):
    return num*2

# Map()
# 1. Takes Each item from the list
# 2. execute the function on it
# 3. Return same number of elements (list)

double_list = list(map(double_item,my_l))
print(double_list)

