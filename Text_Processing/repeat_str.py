"""
reads a sequence of strings, separated by a single space.
Each string should be repeated N times, where N is the length of the string.
Print the final strings concatenated into one string.
"""

in_str = str(input()).split()
for word in in_str:
    n = len(word)
    print(word * n, end='')
