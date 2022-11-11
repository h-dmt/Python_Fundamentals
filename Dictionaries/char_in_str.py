"""
Print all the occurrences in the following format:
"{char} -> {occurrences}"
"""

dct_count = {}

str_in = input()
for char in str_in:
    if char != ' ':
        key = char
        if key in dct_count:
            dct_count[key] += 1
        else:
            dct_count[key] = 1

for k in dct_count:
    print(f"{k} -> {dct_count[k]}")
