"""
You will be given a sequence of strings, each on a new line until you receive the
"stop" command. Every odd line on the console represents a resource
(e.g., Gold, Silver, Copper, and so on) and every even - quantity.
Your task is to collect the resources and print them each on a new line.
Print the resources and their quantities in the following format:
"{resource} -> {quantity}"
"""

mine_dictionary = {}
item = input()
while item != 'stop':
    qty = int(input())
    if item not in mine_dictionary:
        mine_dictionary[item] = qty
    else:
        mine_dictionary[item] += qty
    item = input()

for i in mine_dictionary:
    print(f"{i} -> {mine_dictionary[i]}")
