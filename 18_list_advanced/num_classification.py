"""
Using a list comprehension, write a program that receives numbers,
separated by comma and space ", ", and prints all the positive, negative,
even, and odd numbers on separate lines as shown below.
"""


def positive(num_l):
    positives = []
    for p in num_l:
        if int(p) >= 0:
            positives.append(p)
    return positives


def negative(num_l):
    negatives = []
    for n in num_l:
        if int(n) < 0:
            negatives.append(n)
    return negatives


def even(num_l):
    evens = []
    for e in num_l:
        if int(e) % 2 == 0:
            evens.append(e)
    return evens


def odd(num_l):
    odds = []
    for o in num_l:
        if int(o) % 2 != 0:
            odds.append(o)
    return odds


num_list = input().split(', ')

print(f"Positive: {', '.join(positive(num_list))}")
print(f"Negative: {', '.join(negative(num_list))}")
print(f"Even: {', '.join(even(num_list))}")
print(f"Odd: {', '.join(odd(num_list))}")
