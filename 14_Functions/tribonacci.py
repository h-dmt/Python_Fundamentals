"""
In the Tribonacci sequence, every number is formed by the sum of the previous 3.
Write a function that prints numbers from the Tribonacci sequence on one
 line separated by a single space, starting from 1.
 You will receive a positive integer number as input.
"""


def tribonacci(n):
    tmp_lst = []
    tribonacci_lst = [1]
    next_elem = 0
    while len(tribonacci_lst) < n:
        tmp_lst = tribonacci_lst[-3::]
        for i in tmp_lst:
            next_elem += i
        tribonacci_lst.append(next_elem)
        next_elem = 0
    return tribonacci_lst


num = int(input())
print(*tribonacci(num), sep = " ")

