import re

constrains = r"((^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s)))"

num_input = input().split()
for num in num_input:
    matches = re.search(constrains, num)
    if matches:
        print(matches.group(), end=' ')
