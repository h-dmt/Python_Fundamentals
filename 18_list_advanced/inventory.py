"""
s a young traveler, you gather items and craft new items.
Input / Constraints
You will receive a journal with some collecting items, separated with a comma
and a space (", "). After that, until receiving "Craft!" you will be receiving
different commands split by " - ":
    • "Collect - {item}" - you should add the given item to your inventory.
        If the item already exists, you should skip this line.
    • "Drop - {item}" - you should remove the item from your inventory if it
        exists.
    • "Combine Items - {old_item}:{new_item}" - you should check if the old
        item exists. If so, add the new item after the old one. Otherwise,
        ignore the command.
    • "Renew – {item}" – if the given item exists, you should change its position
    and put it last in your inventory.

Output
After receiving "Craft!" print the items in your inventory, separated by ", ".
"""


def combine(item, lst_in):
    old_item = item[0]
    new_item = item[1]
    in_old_item = lst_in.index(old_item)
    lst_in.insert(in_old_item + 1, new_item)
    return lst_in


def renew(item, lst_in):
    ind_old = lst_in.index(item)
    lst_in.pop(ind_old)
    lst_in.append(item)
    return lst_in


lst_items = input().split(', ')
command = input().split(' - ')
items = []

while command[0] != 'Craft!':
    if command[0] == 'Collect' and command[1] not in lst_items:
        lst_items.append(command[1])

    elif command[0] == 'Drop' and command[1] in lst_items:
        lst_items.remove(command[1])

    elif command[0] == 'Combine Items':
        items = command[1].split(':')
        if items[0] in lst_items:
            lst_items = combine(items, lst_items)

    elif command[0] == 'Renew':
        if command[1] in lst_items:
            lst_items = renew(command[1], lst_items)

    command = input().split(' - ')

print(', '.join(lst_items))
