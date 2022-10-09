"""
a program that receives a sequence of numbers (integers) separated by
a single space. It should print a sorted list of numbers in ascending order.
- Use sorted().
"""

# The sorted() function returns a sorted list of the specified iterable object


def sort_this(lst):
    out_lst = sorted(lst)
    return out_lst


lst_in = input().split()
lst_in = list(map(int, lst_in))
sorted_lst = sort_this(lst_in)
print(sorted_lst)
