# Recursion
# Recursiom is a programming technique where a function calls itesle in order to solve a problem

# Key Concepts
# 1. Base case
# 2. Recursive case

# factorial
# n = 5

def factorial(n):
    # base case:
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n-1)

print(factorial(5))