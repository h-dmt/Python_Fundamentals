import re

egg_pattern = r"(\@+|\#+)([a-z]{3,})(\#+|\@+)[^A-Za-z0-9]*\/+([0-9]+)\/+"
# r"(\@+|\#+)([a-z]{2,})(\@+|\#+)|\1"
# r"\/+([0-9]+)\/+"
some_text = input()
valid_eggs = []
found_eggs = re.findall(egg_pattern, some_text)

for egg in found_eggs:
    combo = (egg[3], egg[1])
    valid_eggs.append(combo)
# print(valid_eggs)

for comb in valid_eggs:
    print(f"You found {comb[0]} {comb[1]} eggs!")
