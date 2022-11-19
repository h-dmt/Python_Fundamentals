"""
He'll give you a series of strings (containing only non-numerical characters)
followed by non-negative numbers (N), e.g., "a3".
You need to convert the letters to uppercase for each string and print it
repeatedly N times on the console. In the example, you need to write back "AAA".
First, on the output, you should print a statistic of the number of unique symbols
used (case-insensitive) in the format: "Unique symbols used {0}".
Next, print the rage message itself.
The strings and numbers will not be separated by anything.
The input will always start with a non-numeric symbol, and for each string,
there will be a corresponding number. The input will be given on a single line.
"""


def count_symbols(mex):
    n = 0
    sym_str = ''
    for letter in mex:
        if letter not in sym_str and not letter.isnumeric():
            sym_str += letter
    n = len(sym_str)
    return n


def symbol_multiplier(symbs, n):
    out_string = symbs * n
    return out_string.upper()


rage_mex = input()
s = ''
x = 0
message = ''
n_sym = count_symbols(rage_mex.upper())
for i in range(len(rage_mex)):
    if not rage_mex[i].isnumeric():  # extract non numeric elements
        s += rage_mex[i]
    elif rage_mex[i].isnumeric():  # find multiplier
        x = rage_mex[i]
        if i < len(rage_mex)-1:  # a check not go out of range
            if rage_mex[i+1].isnumeric():  # if also next element is number
                x += rage_mex[i+1]
        x = int(x)
        message += symbol_multiplier(s, x)  # multiply the string x times
        s = ''
        x = 0
print(f"Unique symbols used: {n_sym}")
print(message)
