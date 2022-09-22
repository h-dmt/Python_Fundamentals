# Write a program that prints part of the ASCII table characters
# on the console, separated by a single space.
# On the first line of input, you will receive the char index
# you should start with.
# On the second line - the index of the last character you should print.

# Use of chr() function

start_point = int(input())
end_point = int(input())
list_chars = []
for i in range(start_point, end_point + 1):
    print(chr(i), end=' ')

"""    list_chars += chr(i)
print(list_chars)"""
