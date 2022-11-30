"""
On the first line of the input, you will receive the concealed message.
After that, until the "Reveal" command is given, you will receive strings with
instructions for different operations that need to be performed upon the concealed
message to interpret it and reveal its actual content.
There are several types of instructions, split by ":|:"
    • "InsertSpace:|:{index}":
        ◦ Inserts a single space at the given index.
           The given index will always be valid.
    • "Reverse:|:{substring}":
        ◦ If the message contains the given substring, cut it out, reverse it and
          add it at the end of the message.
        ◦ If not, print "error".
        ◦ This operation should replace only the first occurrence of the given substring
          if there are two or more occurrences.
    • "ChangeAll:|:{substring}:|:{replacement}":
        ◦ Changes all occurrences of the given substring with the replacement text.

    After the "Reveal" command is received, print this message:
        "You have a new text message: {message}"
"""

message = input()

while True:
    instruction = input().split(':|:')
    if instruction[0] == 'Reveal':
        print(f"You have a new text message: {message}")
        break
    else:
        if instruction[0] == 'InsertSpace':
            ind = int(instruction[1])
            message = message[:ind] + ' ' + message[ind:]
        elif instruction[0] == 'Reverse':
            sub_text = instruction[1]
            sub_rev = sub_text[::-1]
            if sub_text in message:
                message = message.replace(sub_text, '', 1)
                message += sub_rev
            else:
                print('error')
                continue
        elif instruction[0] == 'ChangeAll':
            replace_text = instruction[2]
            remove_str = instruction[1]
            message = message.replace(remove_str, replace_text)
        print(message)
