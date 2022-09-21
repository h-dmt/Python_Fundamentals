string_input = str(input())
indices = str()
for i in range(len(string_input)):
    if str.isupper(string_input[i]):
        indices += str(i) + ', '
indices = indices[0:len(indices)-2]
print(f'[{indices}]')
