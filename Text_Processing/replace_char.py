"""
reads a string from the console and replaces any sequence of the same letters with a single corresponding letter.
"""

str_in = input()
prev_char = ''
txt_out = ''
for curr_char in str_in:
    if curr_char != prev_char:
        txt_out += curr_char
        prev_char = curr_char
print(txt_out)
