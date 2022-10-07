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

lst_in = str(input()).split()
min_odd(lst_in)
