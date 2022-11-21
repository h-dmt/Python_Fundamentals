"""
Write a program that prints the sum of all found characters between two given
characters (their ASCII code). On each of the first two lines,
you will receive a single character. On the last line, you get a random string.
Print the sum of the ASCII values of all characters in the random string between the
two given characters in the ASCII table.
"""

lim_1 = ord(input())
lim_2 = ord(input())
if lim_1 < lim_2:
    lower = lim_1
    higher = lim_2
else:
    lower = lim_2
    higher = lim_2
group_match = []
inp_str = input()
for i in inp_str:
    if lower < ord(i) < higher:
        group_match.append(ord(i))
print(sum(group_match))
