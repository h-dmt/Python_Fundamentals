"""
Write a program that reads usernames on a single line (separated by ", ") and
prints all valid usernames on separate lines.
A valid username:
    • has length between 3 and 16 characters inclusive
    • can contain only letters, numbers, hyphens, and underscores
    • has no redundant symbols before, after, or in between
"""


def length_ok(usr):
    check = False
    if 3 <= len(usr) <= 16:
        check = True
    return check


def symbols_ok(usr):
    check = False
    for i in usr:
        if i.isalpha() or i.isdigit() or i == '-' or i == '_':
            check = True
        else:
            return False
    return check


usernames = input().split(', ')
valid_usr = []
for users in usernames:
    if length_ok(users) and symbols_ok(users):
        valid_usr.append(users)

[print(x) for x in valid_usr]
