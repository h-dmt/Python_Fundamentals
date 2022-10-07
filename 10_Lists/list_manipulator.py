#################################################################################
# The list may be manipulated by one of the following commands:                 #
#     • "exchange {index}" – splits the list after the given index and          #
#     exchanges the places of the two resulting sub-lists.                      #
#     E.g., [1, 2, 3, 4, 5] -> "exchange 2" -> result: [4, 5, 1, 2, 3]          #
#         ◦ If the index is outside the boundaries of the list, print           #
#         "Invalid index"                                                       #
#         ◦ A negative index is considered invalid                              #
#     • "max even/odd"– returns the INDEX of the max even/odd element.          #
#     E.g., [1, 4, 8, 2, 3] -> "max odd" -> print: 4                            #
#     • "min even/odd" – returns the INDEX of the min even/odd element.         #
#     E.g. [1, 4, 8, 2, 3] -> "min even" -> print: 3                            #
#         ◦ If there are two or more equal min/max elements, return the index   #
#         of the rightmost one                                                  #
#         ◦ If a min/max even/odd element cannot be found, print "No matches"   #
#     • "first {count} even/odd" – returns the first count even/odd elements.   #
#     E.g. [1, 8, 2, 3] -> "first 2 even" -> print [8, 2]                       #
#     • "last {count} even/odd" – returns the last count even/odd elements.     #
#     E.g. [1, 8, 2, 3] -> "last 2 odd" -> print [1, 3]                         #
#         ◦ If the count is greater than the list length, print "Invalid count" #
#         ◦ If there are not enough elements to satisfy the count, print as     #
#         many as you can. If there are zero even/odd elements, print an empty  #
#         list "[]"                                                             #
#     • "end" - stop taking input and print the final state of the list         #
#################################################################################
def exchange(lst, ind):
    out_lst = []
    if ind >= len(lst) or ind < 0:
        print("Invalid index")
        lst = list(map(int, lst))
        return lst
    else:
        for i in range(ind + 1, len(lst)):
            out_lst.append(lst[i])
        for j in range(0, ind + 1):
            out_lst.append(lst[j])
        # out_lst = list(map(int, out_lst))
        # print(out_lst)
        return out_lst


def max_even(lst):
    even = False
    even_num = int()
    even_ind = int()
    for i in range(len(lst)):
        if int(lst[i]) % 2 == 0 and int(lst[i]) >= even_num:
            even_num = int(lst[i])
            even_ind = i
            even = True
    if even:
        print(even_ind)
    else:
        print('No matches')


def min_even(lst):
    even = False
    even_num = 1000
    even_ind = int()
    for i in range(len(lst)):
        if int(lst[i]) % 2 == 0 and int(lst[i]) <= even_num:
            even_num = int(lst[i])
            even_ind = i
            even = True
    if even:
        print(even_ind)
    else:
        print('No matches')


def max_odd(lst):
    odd = False
    odd_num = int()
    odd_ind = int()
    for i in range(len(lst)):
        if int(lst[i]) % 2 != 0 and int(lst[i]) >= odd_num:
            odd_num = int(lst[i])
            odd = True
            odd_ind = i
    if odd:
        print(odd_ind)
    else:
        print('No matches')


def min_odd(lst):
    odd = False
    odd_num = 1000
    odd_ind = int()
    for i in range(len(lst)):
        if int(lst[i]) % 2 != 0 and int(lst[i]) <= odd_num:
            odd_num = int(lst[i])
            odd = True
            odd_ind = i
    if odd:
        print(odd_ind)
    else:
        print('No matches')


def first_even(lst, n):
    even_lst = []
    if n > len(lst):
        print('Invalid count')
    else:
        for i in lst:
            if int(i) % 2 == 0 and n > 0:
                even_lst.append(int(i))
                n -= 1
        print(even_lst)


def first_odd(lst, n):
    odd_lst = []
    if n > len(lst):
        print('Invalid count')
    else:
        for i in lst:
            if int(i) % 2 != 0 and n > 0:
                odd_lst.append(int(i))
                n -= 1
        print(odd_lst)


def last_even(lst, n):
    even_lst = []
    if n > len(lst):
        print('Invalid count')
    else:
        for i in range(len(lst) - 1, -1, -1):
            if int(lst[i]) % 2 == 0 and n > 0:
                even_lst.append(int(lst[i]))
                n -= 1
        even_lst.reverse()
        print(even_lst)


def last_odd(lst, n):
    odd_lst = []
    if n > len(lst):
        print('Invalid count')
    else:
        for i in range(len(lst) - 1, -1, -1):
            if int(lst[i]) % 2 != 0 and n > 0:
                odd_lst.append(int(lst[i]))
                n -= 1
        odd_lst.reverse()
        print(odd_lst)


lst_in = input().split()
lst_final = []
command = input().split()
while command[0] != 'end':
    # check max even/odd
    if command[0] + ' ' + command[1] == 'max even':
        max_even(lst_in)
    elif command[0] + ' ' + command[1] == 'max odd':
        max_odd(lst_in)
    # check min even/odd
    if command[0] + ' ' + command[1] == 'min even':
        min_even(lst_in)
    elif command[0] + ' ' + command[1] == 'min odd':
        min_odd(lst_in)
    # check first even/odd
    elif command[0] == 'first':
        if command[2] == 'even':
            first_even(lst_in, int(command[1]))
        else:
            first_odd(lst_in, int(command[1]))
    # check last even/odd
    elif command[0] == 'last':
        if command[2] == 'even':
            last_even(lst_in, int(command[1]))
        else:
            last_odd(lst_in, int(command[1]))
    # check exchange
    elif command[0] == 'exchange':
        lst_in = exchange(lst_in, int(command[1]))

    command = input().split()
lst_final = list(map(int, lst_in))
print(lst_final)
