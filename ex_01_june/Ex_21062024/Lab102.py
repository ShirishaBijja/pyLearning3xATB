my_dict = {'a': 1, 'b': 2, 'a': 23}
print(my_dict)  # O/P:  {'a': 23, 'b': 2}
print(len(my_dict))  # 3

print(list(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))
for k, v in my_dict.items():
    print(k, v)