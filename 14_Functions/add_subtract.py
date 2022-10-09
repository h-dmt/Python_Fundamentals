"""
Write functions named:
    • sum_numbers() that returns the sum of the first two integers
    • subtract() that returns the difference between the returned result of
    the first function and the third integer
Wrap the two functions in a function named add_and_subtract() which will receive
the three numbers as parameters.
Print the result of the subtract() function on the console.
"""


def sum_numbers(n1, n2):
    sum_num = n1 + n2
    return sum_num


def subtract(sum_num, n3):
    res = sum_num - n3
    return res


def add_and_subtract(n1, n2, n3):
    sum_num = sum_numbers(n1, n2)
    res = subtract(sum_num, n3)
    return res


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
result = add_and_subtract(num_1, num_2, num_3)
print(result)
