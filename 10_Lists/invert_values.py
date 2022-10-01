"""
Write a program that receives a single string containing positive
and negative numbers separated by a single space.
Print a list containing the opposite of each number.
"""

string_in = str(input())
lst_opp = []
lst_in = string_in.split()
for i in lst_in:
    opposite = int(i) * -1
    lst_opp.append(opposite)

print(lst_opp)
