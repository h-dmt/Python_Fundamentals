"""
 Write a program that reverses strings and prints each pair on a separate line
 in the format "{word} = {reversed_word}".
"""

in_str = str(input())
while in_str != 'end':
    reverse_str = ''
    # for i in range(len(in_str)-1, -1, -1):
    reverse_str = in_str[::-1]
    print(f"{in_str} = {reverse_str} ")
    in_str = str(input())
