"""
Write a function that receives two characters and returns a single string with
all the characters in between them (according to the ASCII code),
separated by a single space. Print the result on the console.
"""


def between_ascii(ch1, ch2):
    n1 = ord(ch1)
    n2 = ord(ch2)
    list_symb = []
    for i in range(n1 + 1, n2):
        list_symb.append(chr(i))
    return list_symb


char_a = input()
char_b = input()
lst_sym = between_ascii(char_a, char_b)
print(' '.join(lst_sym))
