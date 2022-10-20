"""
You will be given two sequences of strings, separated by ", ".
Print a new list containing only the strings from the first input line,
which are substrings of any string in the second input line.
"""


str_1 = input().split(', ')
str_2 = input().split(', ')
sub_str = []
# Solution with comprehension list - DO NOT USE!
# sub_str = [first for first in str_1 if any(first in second for second in str_2)]

for first in str_1:
    for second in str_2:
        if first in second:
            sub_str.append(first)
            break

print(sub_str)
