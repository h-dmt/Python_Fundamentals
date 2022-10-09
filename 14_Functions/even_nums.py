"""
Write a program that receives a sequence of numbers (integers) separated by
a single space. It should print a list of only the even numbers. Use filter().
"""


def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


lst_in = input().split(' ')
lst_in = list(map(int, lst_in))
# The filter() function extracts elements from an iterable
# (list, tuple etc.) for which a function returns True.
is_even = filter(check_even, lst_in)
even_lst = list(is_even)

print(even_lst)
