energy = 100
coins = 100
event = []
lst_events = str(input()).split('|')
gained_energy = 0
closed = False
for i in lst_events:
    event = i.split('-')
    if event[0] == 'rest':
        if energy == 100:
            gained_energy = 0
        else:
            energy += int(event[1])
            if energy > 100:
                gained_energy = 100 - energy + int(event[1])
                energy = 100
            else:
                gained_energy = int(event[1])
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif event[0] == 'order':
        if energy >= 30:
            coins += int(event[1])
            print(f'You earned {int(event[1])} coins.')
            energy -= 30
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print('You had to rest!')
    else:                                # Have to buy some ingredients
        if coins >= int(event[1]):
            coins -= int(event[1])
            print(f'You bought {event[0]}.')
        else:            # Not enough money to buy ingredients ...
            print(f'Closed! Cannot afford {event[0]}.')
            closed = True
            break
if not closed:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
