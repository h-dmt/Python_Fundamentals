# Write a program to read an integer N and print all triples of the first
# N small Latin letters, ordered alphabetically:
                      # My code
n_letters = int(input())
letter = 97
letter_list = ['a', 'a', 'a']
"""
for l1 in range(0, n_letters):
    letter_list[0] = chr(letter + l1)
    letter_list[1] = 'a'
    letter_list[2] = 'a'
    for l2 in range(0, n_letters):
        letter_list[1] = chr(letter + l2)
        for l3 in range(0, n_letters):
            letter_list[2] = chr(letter + l3)
            print(''.join(letter_list))
"""
#                          # Easier solution
for i in range(0, n_letters):
    for j in range(0, n_letters):
        for k in range(0, n_letters):
            print(f'{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}')
