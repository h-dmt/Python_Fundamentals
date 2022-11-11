"""
The possible items are:
    • "Shadowmourne" - requires 250 Shards
    • "Valanyr" - requires 250 Fragments
    • "Dragonwrath" - requires 250 Motes
"Shards", "Fragments", and "Motes" are the key materials
(case-insensitive), and everything else is junk.

"""


def check_prize(dct):
    reward = False
    coin = ''
    if dct.get('shards') >= 250:
        reward = 'Shadowmourne'
        coin = 'shards'
    if dct.get('fragments') >= 250:
        reward = 'Valanyr'
        coin = 'fragments'
    if dct.get('motes') >= 250:
        reward = "Dragonwrath"
        coin = 'motes'

    return reward, coin


input_items = input().split()
prize = False
junk_items = {}
prize_items = {'shards': 0, 'fragments': 0, 'motes': 0}
while input_items:
    for item in input_items:
        if item.isnumeric():
            qty = int(item)
        else:
            item = item.lower()
            if item in prize_items:
                prize_items[item] += qty
            elif item in junk_items:
                junk_items[item] += qty
            else:
                junk_items[item] = qty
        prize, win_item = check_prize(prize_items)
        if prize:
            prize_items[win_item] -= 250
            print(f"{prize} obtained!")
            break
    if prize:
        break
    input_items = input().split()

for i in prize_items:
    print(f"{i}: {prize_items[i]}")
for j in junk_items:
    print(f"{j}: {junk_items[j]}")
