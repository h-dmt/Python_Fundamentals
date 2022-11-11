"""
Write a program that receives a single string. On the first line, print all the
digits found in the string, on the second – all the letters, and on the third –
all the other characters. There will always be at least one digit, one letter,
and one other character.
"""

in_str = str(input())
digits = ''
letters = ''
others = ''
for i in in_str:
    if i.isalpha():
        letters += i
    elif i.isnumeric():
        digits += i
    else:
        others += i
print(f"{digits}\n{letters}\n{others}")
