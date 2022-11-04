"""
You will receive a single line containing some food (keys) and quantities (values).
 They will be separated by a single space
 (the first element is the key, the second – the value, and so on).
 Create a dictionary with all the keys and values and print it on the console.
"""

items_lst = input().split(' ')
items_dct = {}

for i in range(0, len(items_lst), 2):
    key = items_lst[i]
    value = items_lst[i+1]
    items_dct[key] = int(value)

print(items_dct)
