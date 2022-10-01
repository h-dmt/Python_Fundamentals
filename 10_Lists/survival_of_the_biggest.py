"""
Write a program that receives a list of integer numbers
(separated by a single space) and a number n.
The number n represents the count of numbers to remove from the list.
You should remove the smallest ones, and then, you should print all the
numbers that are left in the list, separated by a comma and a space ", ".
"""

lst_num = str(input()).split()
n = int(input())
smallest = 0
# Transform the list in ints ...
for r in range(len(lst_num)):
    lst_num[r] = int(lst_num[r])
#remove n smallest elemts from list
for k in range(n):
# find the smallest element
    for i in lst_num:
        smallest = i
        for j in lst_num:
            if j < smallest:
                smallest = j
# remove the smallest
    lst_num.remove(smallest)

#Transfoming (again -_-) the list in strings
for s in range(len(lst_num)):
    lst_num[s] = str(lst_num[s])
print(', '.join(lst_num))
