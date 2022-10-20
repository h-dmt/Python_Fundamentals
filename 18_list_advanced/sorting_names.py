"""
Write a program that reads a single string with names separated by comma and
space ", ". Sort the names by their length in descending order.
If 2 or more names have the same length, sort them in ascending order
(alphabetically). Print the resulting list.
"""

names_lst = input().split(', ')
# Use of sorted()
# sorted(iterable, key=None, reverse=False)
# creates a different list!! sort() sorts the current list.
sorted_names = sorted(names_lst, key=lambda item: (-len(item), item))
print(sorted_names)