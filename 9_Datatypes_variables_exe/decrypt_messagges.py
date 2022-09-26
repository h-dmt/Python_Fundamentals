# on the first line, you will receive a key (integer).
# On the second line, you will receive n – the number of lines,
# which will follow. On the next n lines – you will receive a lower
# and an uppercase letter per line.
# You should add the key to each of the characters and append them to a message.
# In the end, print the decrypted message.

key = int(input())
n_char = int(input())
decrypt = ''
char_in = ''
char_ascii = 0
for i in range(n_char):
    char_in = input()
    char_ascii = ord(char_in) + key
    decrypt += chr(char_ascii)
print(decrypt)
