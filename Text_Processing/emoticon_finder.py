"""
An emoticon always starts with ":" and is followed by a symbol.
The input will be provided as a single string.
"""

txt_in = input()
emojis = []
for i in range(len(txt_in)-1):
    if txt_in[i] == ':':
        emoji = ':' + txt_in[i+1]
        emojis.append(emoji)
[print(x) for x in emojis]
