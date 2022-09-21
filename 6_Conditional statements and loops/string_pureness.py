n = int(input())
for _ in range(n):
    word = str(input())
    pure = True
    for i in word:
        if i == ',' or i == '.' or i == '_':
            pure = False
            print(f'{word} is not pure!')
            break
    if pure:
        print(f'{word} is pure.')
