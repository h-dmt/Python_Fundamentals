#getting the list of itemes
lst_items = str(input()).split('|')
item = []
budget = float(input())
buy_list = []
top_clothes = 50
top_shoes = 35
top_accessories = 20.50
sell_lst = []
spent = 0
profit = 0
income = 0
# buying the stuff
for i in lst_items:
    item = i.split('->')
    if (item[0] == 'Clothes' and float(item[1]) <= top_clothes)\
            or (item[0] == 'Shoes' and float(item[1]) <= top_shoes)\
            or (item[0] == 'Accessories' and float(item[1]) <= top_accessories):
        if budget >= float(item[1]):
            spent += float(item[1])
            budget -= float(item[1])
            buy_list.append(float(item[1]))
        else:
            continue
# selling the stuff:
for j in buy_list:
    income += j * 1.4
    sell_lst.append("%.2f" % (j * 1.4))

budget = budget + income
profit = income - spent
print(' '.join(sell_lst))
print(f'Profit: {profit:.2f}')
if budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
