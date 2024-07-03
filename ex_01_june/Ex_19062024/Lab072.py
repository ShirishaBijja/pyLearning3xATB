# Important Question

numbers = [1, 2, 3]

# List is a collection of items


def do_something(pramod_lists):
    pramod_lists.append(100)
    pramod_lists[0] = 124
    return pramod_lists

numbers.append(10)    # 1,2,3,10
l = do_something(numbers)
print(l)     # O/p: 124, 2, 3, 10, 100
