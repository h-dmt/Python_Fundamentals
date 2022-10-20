"""
You are given a secret message you should decipher.
To do that, you need to know that in each word:
    • the second and the last letter are switched (e.g., Holle means Hello)
    • the first letter is replaced by its character code (e.g., 72 means H)
"""


def decypher(crypt_str):
    crypt_str[0] = chr(int(crypt_str[0]))
    tmp = crypt_str[-1]
    crypt_str[-1] = crypt_str[1]
    crypt_str[1] = tmp
    return ''.join(crypt_str)


def find_digits(w_in):
    num = ''
    pop_index = 0
    check_num = False
    for k in range(len(w_in) - 1):
        if w_in[k].isdigit():
            num += w_in[k]
            pop_index += 1
            check_num = True
    if check_num:
        del w_in[0:pop_index]
        w_in.insert(0, num)
    # print(''.join(w_in))
    return w_in


crypted_mex = input().split(' ')
decrypted_mex = []
for word in crypted_mex:
    lst_word = list(word)
    lst_word = find_digits(lst_word) # searches for int in the list
    decrypted_mex.append(decypher(lst_word)) # deciphers the message
print(*decrypted_mex, sep=' ')
