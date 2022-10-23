"""
You will receive a single input line containing strings, separated by spaces.
The strings may contain any ASCII character except whitespace.
Then you will begin receiving commands in one of the following formats:
    • merge {startIndex} {endIndex}
    • divide {index} {partitions}
Every time you receive the merge command, you must merge all elements from the
startIndex to the endIndex. In other words, you should concatenate them.
Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}
If any of the given indexes is out of the array, you must take only the range
that is inside the array and merge it.
Every time you receive the divide command, you must divide the element at the
given index into several small substrings with equal length.
The count of the substrings should be equal to the given partitions.
Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
If the string cannot be exactly divided into the given partitions,
make all partitions except the last with equal lengths and make the last one -
the longest.
Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
The input ends when you receive the command "3:1". At that point, you must print the resulting elements,
joined by a space.
"""


def merge_fun(lst_in, start, end):
    if end >= len(lst_in):
        end = len(lst_in) - 1
    if start > len(lst_in):
        start = end - 1
    merge_str = ''.join(lst_in[start:end+1])
    del lst_in[start:end+1]
    lst_in.insert(start, merge_str)

    return lst_in


def divide_fun(str_in, parts):
    in_list = str_in
    splpit = []
    n = 0
    if parts >= len(in_list):
        n = 1
        parts = len(in_list)
        last_cunk = len(in_list) - n*(parts - 1)
        splpit = [in_list[i:i + n] for i in range(0, len(in_list) - last_cunk, n)]
        splpit.append(in_list[len(in_list) - last_cunk:])

    elif len(in_list) % parts != 0:
        n = len(in_list) // parts
        last_cunk = len(in_list) - n*(parts - 1)
        splpit = [in_list[i:i+n] for i in range(0, len(in_list) - last_cunk, n)]
        splpit.append(in_list[len(in_list) - last_cunk:])

    elif len(in_list) % parts == 0:
        # lenght of every chunk
        n = len(in_list) // parts
        #last_cunk = len(in_list) - n*(parts-1)
        splpit = [in_list[i:i+n] for i in range(0, len(in_list), n)]
        #splpit.append(in_list[len(in_list) - last_cunk::])

    return splpit


in_lst = input().split()
command = input().split()
out_lst = []
index_div = 0
div_elements = []

while command[0] != '3:1':
    if command[0] == 'merge':
        out_lst = merge_fun(in_lst, int(command[1]), int(command[2]))
        #print(out_lst)
    elif command[0] == 'divide':
        index_div = int(command[1])
        #print(in_lst[index_div])
        div_elements = divide_fun(in_lst[index_div], int(command[2]))
        #print(div_elements)
        del in_lst[index_div]
        for i in range(len(div_elements)):
            in_lst.insert(index_div + i, div_elements[i])
    #print(in_lst)
    command = input().split()

print(*out_lst, sep=' ')
