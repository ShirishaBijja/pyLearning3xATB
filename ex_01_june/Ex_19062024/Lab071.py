numbers = [1, 2, 3]

# List is a collection of items


def do_something(numbers):
    numbers.append(4)
    numbers[0] = 100
    return numbers


l = do_something(numbers)
print(l)
