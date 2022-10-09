"""
Write a function that receives three integer numbers and returns the smallest.
Print the result on the console. Use an appropriate name for the function.
"""


def smallest(lst):
    smal = lst[0]
    for i in lst:
        if i < smal:
            smal = i
    return smal


lst_in = []
for i in range(3):
    lst_in.append(input())
lst_in = list(map(int, lst_in))
# min_num = smallest(lst_in)
print(smallest(lst_in))
