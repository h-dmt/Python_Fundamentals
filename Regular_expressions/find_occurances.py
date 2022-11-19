"""
Write a program that finds how many times a word is used in a string.
The output is a single number indicating the number of times the string contains
the word. Note that letter case does not matter – it is case-insensitive.
"""

import re

in_text = input()
key = input()

regex = fr'\b{key}\b'
repetitions = re.findall(regex, in_text, re.IGNORECASE)
print(len(repetitions))
