"""
You will receive a single number.
You should write a function that returns the sum of all even and all odd
digits in a given number. The result should be returned as a single string
in the format:
"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
Print the result of the function on the console.
"""


def sum_of_odd(lst_n):
    sum_odds = 0
    for i in lst_n:
        if i % 2 != 0:
            sum_odds += i
    return sum_odds


def sum_of_even(lst_n):
    sum_even = 0
    for i in lst_n:
        if i % 2 == 0:
            sum_even += i
    return sum_even


num_lst = list(input())
num_lst = list(map(int, num_lst))
evens = sum_of_even(num_lst)
odds = sum_of_odd(num_lst)
print(f'Odd sum = {odds}, Even sum = {evens}')
