"""
https://judge.softuni.org/Contests/Practice/Index/2302#0

Until the "Generate" command is given, you will be receiving strings with instructions for different operations that need to be performed upon the raw activation key.
There are several types of instructions, split by ">>>":
    • "Contains>>>{substring}":
        ◦ If the raw activation key contains the given substring, prints: "{raw activation key} contains {substring}".
        ◦ Otherwise, prints: "Substring not found!"
    • "Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
        ◦ Changes the substring between the given indices (the end index is exclusive) to upper or lower case and then prints the activation key.
        ◦ All given indexes will be valid.
    • "Slice>>>{startIndex}>>>{endIndex}":
        ◦ Deletes the characters between the start and end indices (the end index is exclusive) and prints the activation key.
        ◦ Both indices will be valid.
"""


def flip(raw_activation_key, flip_command, start_index, end_index):
    # Changes the substring between the given indices (the end index is exclusive)
    # Check valid indexes!!
    if 0 <= start_index < end_index <= len(raw_activation_key):
        substring = raw_activation_key[start_index:end_index]

        if flip_command == 'Upper':
            raw_activation_key = raw_activation_key.replace(substring, substring.upper())
        elif flip_command == 'Lower':
            raw_activation_key = raw_activation_key.replace(substring, substring.lower())

    return raw_activation_key


def slice_key(raw_activation_key, start_index, end_index):
    # Deletes the characters between the start and end indices
    if 0 <= start_index < end_index <= len(raw_activation_key):
        delete_str = raw_activation_key[start_index:end_index]
        raw_activation_key = raw_activation_key.replace(delete_str, '')

    return raw_activation_key


raw_activation_key = input()
activation_key = raw_activation_key
commands = input().split('>>>')
while commands[0] != 'Generate':
    if commands[0] == 'Contains':
        # If the raw activation key contains the given substring, prints:
        # "{raw activation key} contains {substring}"
        # else "Substring not found!"
        substring = commands[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")

    if commands[0] == 'Flip':
        start_index = int(commands[2])
        end_index = int(commands[3])  # not included!!
        flip_command = commands[1]
        raw_activation_key = flip(raw_activation_key, flip_command, start_index, end_index)
        print(raw_activation_key)

    if commands[0] == 'Slice':
        start_index = int(commands[1])
        end_index = int(commands[2])
        raw_activation_key = slice_key(raw_activation_key, start_index, end_index)
        print(raw_activation_key)

    commands = input().split('>>>')
activation_key = raw_activation_key
print(f"Your activation key is: {activation_key}")
