"""
    On the first line, you will receive a key (sequence of numbers separated by a space).
    On the next few lines, you will receive lines with strings until you get the command
    "find".
    You should loop through every string and decrease the ASCII code of each character
    with a corresponding number of the key sequence. You choose a key number from the
    sequence by just looping through it. If the length of the key sequence is less than
    the string sequence, you should continue looping from the beginning.
    For more clarification, see the example below.
    After decrypting the message, you will get a type of treasure and its coordinates.
    The type will be between the symbol "&", and the coordinates -
    between the symbols "<' and '>'.
    For each line print the type and the coordinates in the format
    "Found {type} at {coordinates}".
"""
import re


def txt_ascii(txt):
    ascii_out = []
    for i in txt:
        ascii_out.append(ord(i))
    return ascii_out


def decrypt(text, keys):
    ascii_list = txt_ascii(text)  # <-- LIST!!
    text_decrypt = ''
    index = 0
    for element in ascii_list:
        if index >= len(keys):
            index = 0
        text_decrypt += chr(element - int(keys[index]))
        index += 1

    return text_decrypt


key = input().split(' ')
encrypted_mex = input()
type_pattern = r"&(\w+)\&"
coordinates_pattern = r"<(\w+)\>"

while encrypted_mex != 'find':
    mex = decrypt(encrypted_mex, key)
    encrypted_mex = input()
    type_found = re.findall(type_pattern, mex)
    coordinates = re.findall(coordinates_pattern, mex)
    print(f"Found {type_found[0]} at {coordinates[0]}")
