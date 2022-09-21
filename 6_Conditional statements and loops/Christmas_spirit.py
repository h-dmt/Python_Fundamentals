qty_per_shop = int(input())
day_to_chrismas = int(input())
ornament_price = 2
ornament_points = 5
tree_skirt_price = 5
tree_skirt_points = 3
tree_garland_price = 3
tree_garland_points = 10
tree_lights_price = 15
tree_lights_points = 17
expence = 0
spirit = 0
count_second = 0
count_third = 0
count_fifth = 0
count_tent = 0
count_elevent = 0
for i in range(1, day_to_chrismas+1):
    count_second += 1
    count_third += 1
    count_fifth += 1
    count_tent += 1
    count_elevent += 1
    if count_elevent == 11:
        qty_per_shop += 2
        count_elevent = 0
#Day 2
    if count_second == 2:
        expence += ornament_price * qty_per_shop
        spirit += ornament_points
        if count_tent == 10:
            expence += tree_skirt_price + tree_garland_price + tree_lights_price
            spirit -= 20
            count_tent = 0
        count_second = 0

# Day 3
    if count_third == 3:
        expence += (tree_skirt_price + tree_garland_price) * qty_per_shop
        spirit += tree_skirt_points + tree_garland_points
        if count_tent == 10:
            expence += tree_skirt_price + tree_garland_price + tree_lights_price
            spirit -= 20
            count_tent = 0
        count_third = 0

# Day 5
    if count_fifth == 5:
        expence += tree_lights_price * qty_per_shop
        spirit += tree_lights_points
        if (i / 3) % 5 == 0:
            spirit += 30
        if count_tent == 10:
            expence += tree_skirt_price + tree_garland_price + tree_lights_price
            spirit -= 20
            count_tent = 0
        count_fifth = 0

if day_to_chrismas % 10 == 0:
    spirit -= 30

print(f'Total cost: {expence}')
print(f'Total spirit: {spirit}')
