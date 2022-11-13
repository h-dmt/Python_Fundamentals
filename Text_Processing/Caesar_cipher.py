"""
Encrypt the text by replacing each character with the corresponding character
three positions forward in the ASCII table. For example, A would be replaced
with D, B would become E, and so on. Print the encrypted text.
"""


def encrypt(text):
    encrypted = ''
    for i in text:
        encrypted += chr(ord(i) + 3)
    return encrypted


in_txt = str(input())
hidden_txt = encrypt(in_txt)
print(hidden_txt)

