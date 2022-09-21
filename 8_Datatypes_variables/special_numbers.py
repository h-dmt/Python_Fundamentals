"""
Write a program that reads an integer n. Then, for all numbers in the range [1, n],
prints the number and if it is special or not (True / False).
A number is special when the sum of its digits is 5, 7, or 11.
"""
number = int(input())
sum_num = 0
special = False
for i in range(1, number+1):
    for j in str(i):
        sum_num += int(j)
    if sum_num == 5 \
        or sum_num == 7 \
        or sum_num == 11:
        special = True
    else:
        special = False
    sum_num = 0
    print(f'{i} -> {special}')
