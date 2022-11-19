"""
For the given string, you should perform different mathematical operations to achieve a result:
    • First, if the letter in front of the number is:
        ◦ Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
        ◦ Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
    • Next, if the letter after the number is:
        ◦ Uppercase: subtract its position from the resulting number (starting from 1)
        ◦ Lowercase: add its position to the resulting number (starting from 1)

Input
    • The input comes from the console as a single line, holding a sequence of strings
    • Strings are separated by one or more white spaces
    • The input data will always be valid. There is no need to check it explicitly
Output
    • Print at the console a single number:
        ◦ The total sum of all processed numbers, formatted to the second decimal separator
"""


def change(l1, n, l2):
    total = 0
    if l1.isupper():  # If first letter is upper, divide
        total = n / (ord(l1)-64)
    elif l1.lower():  # If first letter is lower, multiply
        total = n * (ord(l1)-96)
    if l2.isupper():  # if second letter is upper, subtract
        total -= (ord(l2)-64)
    elif l2.islower():  # if second letter is lower, add
        total += (ord(l2)-96)

    return total


combos = input().split()
num = int()
lett_1 = ''
lett_2 = ''
tot_sum = 0
for sequence in combos:
    lett_1 = sequence[0]
    lett_2 = sequence[-1]
    num = int(sequence[1:-1])
    tot_sum += change(lett_1, num, lett_2)

print(f"{tot_sum:.2f}")
