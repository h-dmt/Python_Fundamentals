budget = float(input())
flour_price_kg = float(input())
egg_price = 0.75 * flour_price_kg
milk_price = 1.25 * flour_price_kg
bread_price = egg_price + flour_price_kg + 0.250 * milk_price
expence = bread_price
n_bread = 0
color_eggs = 0
count = 0
money_left = budget
while expence < budget:
    n_bread += 1
    color_eggs += 3
    count += 1
    if count == 3:
        color_eggs -= (n_bread - 2)
        count = 0
    money_left = budget - expence
    expence += bread_price

print(f'You made {n_bread} loaves of Easter bread! '
      f'Now you have {color_eggs} eggs and {money_left:.2f}BGN left.')
