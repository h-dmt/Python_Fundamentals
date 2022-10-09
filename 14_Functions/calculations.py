"""
The input comes as three parameters – an operator as a string and two
integer numbers. The operator can be one of the following:
"multiply", "divide", "add", "subtract".
"""


def multiply(a, b):
    res = a * b
    return res


def divide(a, b):
    res = a // b
    return res


def add(a, b):
    res = a + b
    return res


def subtract(a, b):
    res = a - b
    return res


fun_map = {'multiply': multiply, 'divide': divide, 'add': add,
           'subtract': subtract}
operation = input()
n1 = int(input())
n2 = int(input())
if operation in fun_map.keys():
    print(fun_map[operation](n1, n2))
