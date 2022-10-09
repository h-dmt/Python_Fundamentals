"""
Write a function that receives two integer numbers.
Calculate the factorial of each number.
Divide the first result by the second and print the division formatted to
the second decimal point.
"""


def factorial(num):
    factorial_n = 1
    for i in range(1, num + 1):
        factorial_n *= i
    return factorial_n


def fact_divider(n1, n2):
    res = n1 / n2
    return res


num_1 = int(input())
num_2 = int(input())
fact_1 = factorial(num_1)
fact_2 = factorial(num_2)
resoult = fact_divider(fact_1, fact_2)
print(f'{resoult:.2f}')
