# https://judge.softuni.org/Contests/Practice/Index/2303#2
# 26-11-22
# "{hero name} {HP} {MP}"

def cast_spell(dct_heroes, hero, mp_needed, spell):
    if dct_heroes[hero][1] >= mp_needed:
        print(f"{hero} has successfully cast "
              f"{spell} and now has {dct_heroes[hero][1] - mp_needed} MP!")
        dct_heroes[hero][1] -= mp_needed
    else:  # not enough MP
        print(f"{hero} does not have enough MP to cast {spell}!")
    return dct_heroes


def take_damage(dct_heros, hero, hero_damage, attacker_name):
    if dct_heros[hero][0] - hero_damage <= 0:
        print(f"{hero} has been killed by {attacker_name}!")
        del dct_heros[hero]  # hero killed and removed from dictionary
    else:
        print(f"{hero} was hit for {hero_damage} HP by {attacker_name} "
              f"and now has {dct_heros[hero][0] - hero_damage} HP left!")
        dct_heros[hero][0] -= hero_damage
    return dct_heros


def recharge(dct_heroes, name, amount):
    old_amount = dct_heroes[name][1]
    dct_heroes[name][1] += amount
    if dct_heroes[name][1] > 200:
        dct_heroes[name][1] = 200
    recharge_amount = dct_heroes[name][1] - old_amount
    print(f"{name} recharged for {recharge_amount} MP!")
    return dct_heroes


def heal(dct_heroes, name, amount):
    old_amount = dct_heroes[name][0]
    dct_heroes[name][0] += amount
    if dct_heroes[name][0] > 100:
        dct_heroes[name][0] = 100
    recharge_amount = dct_heroes[name][0] - old_amount
    print(f"{name} healed for {recharge_amount} HP!")
    return dct_heroes


n = int(input())
collection_heroes = {}
for _ in range(n):
    splited_input = input().split(' ')
    hero_name = splited_input[0]
    HP = int(splited_input[1])
    MP = int(splited_input[2])
    collection_heroes[hero_name] = [HP, MP]

while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break

    elif command[0] == 'CastSpell':
        name = command[1]
        mp_spell = int(command[2])
        spell_name = command[3]
        collection_heroes = cast_spell(collection_heroes, name, mp_spell, spell_name)

    elif command[0] == 'TakeDamage':
        name = command[1]
        damage = int(command[2])
        attacker = command[3]
        collection_heroes = take_damage(collection_heroes, name, damage, attacker)

    elif command[0] == 'Recharge':
        name, amount = command[1:]
        amount = int(amount)
        collection_heroes = recharge(collection_heroes, name, amount)

    elif command[0] == 'Heal':
        name, amount = command[1:]
        amount = int(amount)
        collection_heroes = heal(collection_heroes, name, amount)

for survived in collection_heroes:
    print(survived)
    print(f"  HP: {collection_heroes[survived][0]}")
    print(f"  MP: {collection_heroes[survived][1]}")
