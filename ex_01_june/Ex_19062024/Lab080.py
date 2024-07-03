list = [1,2,3,4]
#print(list*2)   # [1, 2, 3, 4, 1, 2, 3, 4]


temp_list = []
for i in list:
    # temp = i*2
    # temp_list.append(temp)
    temp_list.append(i*2)
print(temp_list)