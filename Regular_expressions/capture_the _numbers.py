"""
Write a program that receives strings on different lines and extracts only the numbers.
Print all extracted numbers on a single line, separated by a single space.
"""
import re

in_string = input()

regex = '\d+'

while in_string:
    numbers = re.findall(regex, in_string)
    if numbers:
        print(' '.join(numbers), end=' ')
    in_string = input()

