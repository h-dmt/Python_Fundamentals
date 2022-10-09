"""
 The function should check if each integer is
 a palindrome - True or False. Print the result.
"""


def check_palindrome(a):
    if a[0] == a[len(a) - 1]:
        return True
    return False


in_lst = input().split(', ')

for num in in_lst:
    if check_palindrome(num):
        print('True')
    else:
        print('False')
