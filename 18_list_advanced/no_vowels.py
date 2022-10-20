"""
Using comprehension, write a program that receives a text and removes all
its vowels, case insensitive. Print the new text string after removing the vowels.

The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.
"""

in_str = input()
vowels = ['a', 'o', 'u', 'e', 'i']
out_lst = [i for i in in_str if i.lower() not in vowels]

print(''.join(out_lst))
