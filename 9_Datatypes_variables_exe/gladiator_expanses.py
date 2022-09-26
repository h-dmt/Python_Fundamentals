# As a gladiator, Peter needs to repair his broken equipment
# when he loses a fight. His equipment consists of
# a helmet, a sword, a shield, and an armor.
# You will receive Peter's lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight,
# his shield also breaks.
# Every second time his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment.
# Calculate his expenses for the year for renewing his equipment.

lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_broke_count = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0: # broken helmet
        expenses += helmet_price
        if i % 3 == 0: # broken shield
            expenses += shield_price
            shield_broke_count += 1
            if shield_broke_count == 2: # broken armor
                expenses += armor_price
                shield_broke_count = 0
    if i % 3 == 0: # broken sword
        expenses += sword_price

print(f'Gladiator expenses: {expenses:.2f} aureus')
