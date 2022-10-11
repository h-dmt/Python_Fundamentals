"""
Write a function that, depending on the first line of the input, reads one of the
following strings:"int","real", or"string".
    • If the data type is an int, multiply the number by 2.
    • If the data type is real, multiply the number by 1.5 and format the result
        to the second decimal point.
    • If the data type is a string, surround the input with "$".
Print the result on the console.
"""


def data_type(a, d):
    if a == 'int':
        return int(d) * 2
    elif a == 'real':
        return f"{float(d) * 1.5:.2f}"
    elif 'string':
        return sting_format(d)


def sting_format(s):
    return '$' + s + '$'


inp = input()
b = input()
print(data_type(inp, b))
