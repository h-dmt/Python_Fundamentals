"""
Write a program that reads a single string with numbers separated by comma
and space ", ". Print the indices of all even numbers.
"""

lst_num = list(map(int, input().split(', ')))

indices = [num for num in range(len(lst_num)) if lst_num[num] % 2 == 0]
print(indices)
