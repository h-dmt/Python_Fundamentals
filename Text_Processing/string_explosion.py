"""
    • Explosions marked with '>'
    • Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
    • Any other characters
Your task is to delete x characters, starting after the exploded character ('>').
If you find another explosion mark ('>') while deleting characters, you should add the strength to your previous explosion.
You should not delete the explosion character – '>'.
"""


in_str = input()
n = 0
out_str = ''
for i in range(len(in_str)):

    if in_str[i] != '>' and n == 0:
        out_str += in_str[i]
    elif in_str[i] == '>':
        out_str += '>'
        n += int(in_str[i + 1])
    else:
        n -= 1
print(out_str)
