"""
Write a program to read a sequence of integers and find and print the top
5 numbers greater than the average value in the sequence, sorted in descending
order.
Input
    • Read from the console a single line holding space-separated integers.
Output
    • Print the above-described numbers on a single line, space-separated.
    • If less than 5 numbers hold the property mentioned above, print less than 5 numbers.
    • Print "No" if no numbers hold the above property.
Constraints
    • All input numbers are integers in the range [-1000000 … 1000000].
    • The count of numbers is in the range [1…10 000].
"""


def average(lst_in):
    tot = 0
    avg = 0
    for i in lst_in:
        tot += i
    avg = tot // len(lst_in)
    return avg


def top_five(lst_n):
    top_lst = []
    av_value = average(lst_n)
    for j in lst_n:
        if j > av_value:
            top_lst.append(j)
    if len(top_lst) == 0:
        return "No"
    else:
        top_lst.sort()
        return top_lst[-5::]


num_in = input().split(' ')
num_in = list(map(int, num_in))
top_output = top_five(num_in)
if isinstance(top_output, str):
    print(top_output)
else:
    top_output.reverse()
    print(*top_output, sep=" ")
