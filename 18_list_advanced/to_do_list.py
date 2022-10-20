"""
You will be receiving to-do notes until you get the command "End".
The notes will be in the format: "{importance}-{note}".
Return a list containing all to-do notes sorted by importance in ascending order.
The importance value will always be an integer between 1 and 10 (inclusive).
"""

to_do_list = []
sorted_to_do = []
comand = input().split('-')
while comand[0] != 'End':

    priority = int(comand[0])
    current_task = comand[1]
    to_do_list.append([priority, current_task])
    comand = input().split('-')
sorted_to_do = [to_do_list[1] for to_do_list in sorted(to_do_list)]
print(sorted_to_do)
