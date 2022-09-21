n_mess = int(input())

for _ in range(n_mess):
    message = int(input())
    if message == 88:
        print('Hello!')
    elif message == 86:
        print('How are you?')
    elif message < 88:
        print('GREAT!')
    else:
        print('Bye.')
