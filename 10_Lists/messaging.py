"""
On the first line, you will receive a sequence of numbers separated by a single space.
On the second line, you will receive a string.
Your task is to write a program that sends a message only using chars from the given
string. Each char the program adds to the message should be found by its index.
The index you are looking for is the sum of a number's digits from the first sequence.
If the index is greater than the length of the text, continue counting from the
beginning (so that you always have a valid index).
When you find a char, you should add it to the message and remove it from the string.
It means that for the following index, the text will contain one character less.
"""

num_lst = str(input()).split()
in_str = str(input())
tmp_str = str()
lst_index = []
lst_num_index = []
message = str()
index = 0
for i in num_lst:
    # Creating a list for index from the list
    lst_index = list(str(i))
    # Creating the index by summing each element of sub list
    for k in lst_index:
        index += int(k)
    # in case the index exceeds the length of list start again from first element
    while index >= len(in_str):
        index -= len(in_str)
    # Creating the message
    if index >= 0: # <---- A useless check ?? Anyway...
        message += in_str[index]
    # Removing indexed element from the string:
    for j in range(len(in_str)):
        if j != index:
            tmp_str += in_str[j]
    in_str = ''
    in_str = tmp_str
    tmp_str = ''
    index = 0
print(message)
