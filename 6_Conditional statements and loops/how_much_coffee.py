coffe_quant = 0
event = str(input())
while event != 'END':
    if event == 'coding' or event == 'dog' or event == 'cat' or event == 'movie':
        coffe_quant += 1
    elif event == 'CODING' or event == 'DOG' or event == 'CAT' or event == 'MOVIE':
        coffe_quant += 2
    event = str(input())
if coffe_quant > 5:
    print('You need extra sleep')
else:
    print(coffe_quant)