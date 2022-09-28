"""
On the first line, you will receive a number n.
On the second line, you will receive a word.
On the following n lines, you will be given some strings.
You should add them to a list and print them.
After that, you should filter out only the strings that include the given word
and print that list too.
"""
n_strings = int(input())
key_word = str(input())
lst_strings = []
lst_keys = []

for i in range(n_strings):
    lst_strings.append(str(input()))
    if key_word in lst_strings[i]:
        lst_keys.append(lst_strings[i])
print(lst_strings)
print(lst_keys)
