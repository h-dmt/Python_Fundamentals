"""
Write a program that rounds all the given numbers, separated by a single space,
and prints the result as a list. Use round()
"""


def rounding(lst):
    ls_out = lst
    for i in range(0, len(lst)):
        ls_out[i] = round(float(ls_out[i]))
    return ls_out


lst_in = input().split(' ')
print(rounding(lst_in))
