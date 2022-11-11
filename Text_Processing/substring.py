"""
On the first line, you will receive a string.
On the second line, you will receive a second string. Write a program
that removes all the occurrences of the first string in the second until
there is no match. At the end, print the remaining string.
"""

str1 = str(input())  # to be removed
str2 = str(input())
print(str2)
while str1 in str2:
    str2 = str2.replace(str1, '')
print(str2)
