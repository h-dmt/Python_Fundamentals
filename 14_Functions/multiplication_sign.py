"""
You will receive three integer numbers.
Write a program that finds if their multiplication (the result) is negative,
positive, or zero. Try to do this WITHOUT multiplying the 3 numbers.
"""


def sign(a, b, c):
    if a > 0 and b > 0 and c > 0 or \
            a < 0 and b < 0 and c > 0 or\
            a < 0 and c < 0 and b > 0 or\
            b < 0 and c < 0 and a > 0:
        return "positive"
    elif a == 0 or b == 0 or c == 0:
        return "zero"
    else:
        return "negative"


n1 = int(input())
n2 = int(input())
n3 = int(input())
print(sign(n1, n2, n3))
