# LeetCode - sum of digits

number = 12345
# n1 = 12345 // 10
# n2 = 12345 % 10
# sum_of_digits = 15
# print(n1)
# print(n2)

def sum_of_digits(n):
    # base case
    if n<10:
        return n
    # recursive case
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(12345))