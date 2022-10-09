"""
Write a program that receives a sequence of numbers, separated by a
single space, and prints their absolute value as a list. Use abs().
"""


def abs_value(lst):
    abs_lst = []
    for i in lst:
        abs_lst.append(abs(i))
    return abs_lst


lst_in = input().split()
lst_in = list(map(float, lst_in))
abs_list = abs_value(lst_in)
print(abs_list)
