

def to_left(l_side, lim_price, type_item):
    damage = 0
    if type_item == 'cheap':
        for i in l_side:
            if i < lim_price:
                damage += i
    elif type_item == 'expensive':
        for j in l_side:
            if j >= lim_price:
                damage += j
    return damage


def to_right(r_side, lim_price, type_item):
    damage = 0
    if type_item == 'cheap':
        for i in r_side:
            if i < lim_price:
                damage += i
    elif type_item == 'expensive':
        for j in r_side:
            if j >= lim_price:
                damage += j
    return damage


price_ratings_list = list(map(int, input().split(', ')))
entry_point = int(input())
item_type = input()
right_side = price_ratings_list[entry_point + 1:]
left_side = price_ratings_list[:entry_point]
tot_damage = 0
entry_price = price_ratings_list[entry_point]

left_damage = to_left(left_side, entry_price, item_type)
right_damage = to_right(right_side, entry_price, item_type)

if left_damage >= right_damage:
    print(f"Left - {left_damage}")
else:
    print(f"Right - {right_damage}")
