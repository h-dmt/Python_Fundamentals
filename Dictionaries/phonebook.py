"""
Each entry should have a name and a number (both strings) separated by a "-".
If you receive a name that already exists in the phonebook, update its number.
After filling the phonebook, you will receive a number – N. Your program should
be able to perform a search of contact by name and print its details in the format:
"{name} -> {number}". In case the contact isn't found, print:
"Contact {name} does not exist."
"""

entry = input().split('-')
rubrica = {}
while len(entry) > 1:
    name = entry[0]
    phone = entry[1]
    rubrica[name] = phone
    entry = input().split('-')
for _ in range(int(entry[0])):
    contact = input()
    if contact in rubrica:
        print(f"{contact} -> {rubrica[contact]}")
    else:
        print(f"Contact {contact} does not exist.")
