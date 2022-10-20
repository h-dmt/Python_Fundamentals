"""
Write a program that receives a sequence of numbers
(a string containing integers separated by ", ") and prints the numbers sorted into
lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
Examples:
    • The numbers 2, 8, 4, and 10 fall into the group of 10's.
    • The numbers 13, 19, 14, and 15 fall into the group of 20's.
For more clarification, see the examples below.
"""


def grouping(n_lst, g):
    filtered_lst = []
    lst_out = n_lst[:]
    for k in n_lst:
        if k <= g:
            filtered_lst.append(k)
            lst_out.remove(k)
    return filtered_lst, lst_out


num_lst = list(map(int, input().split(', ')))
group_lst = list()

for gr in range(10, max(num_lst) + 10, 10):
    group_lst, num_lst = grouping(num_lst, gr)
    print(f"Group of {gr}'s: {group_lst}")
    group_lst = list()
