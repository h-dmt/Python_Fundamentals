#  https://judge.softuni.org/Contests/Practice/Index/2302#2


def plunder(targets, town, n_people, gold_q):
    # If any of those two values (population or gold) reaches zero,
    # the town is disbanded.
    if targets[town][0] <= n_people:
        killed = targets[town][0]
        stolen_gold = gold_q
        if targets[town][1] <= gold_q:
            stolen_gold = targets[town][1]

        print(f"{town} plundered! {stolen_gold} gold stolen, {killed} citizens killed.")
        print(f"{town} has been wiped off the map!")
        targets.pop(town)
        return targets

    elif targets[town][1] <= gold_q:
        stolen_gold = targets[town][1]
        killed = n_people
        if targets[town][0] <= n_people:
            killed = targets[town][0]

        print(f"{town} plundered! {stolen_gold} gold stolen, {killed} citizens killed.")
        print(f"{town} has been wiped off the map!")
        targets.pop(town)
        return targets

    else:
        killed = n_people
        stolen_gold = gold_q
        targets[town][0] = targets[town][0] - n_people
        targets[town][1] = targets[town][1] - gold_q
        print(f"{town} plundered! {stolen_gold} gold stolen, {killed} citizens killed.")

    return targets


def prosper(targets, town, gold_q):
    targets[town][1] += gold_q
    print(f"{gold_q} gold added to the city treasury. {town} now has {targets[town][1]} gold.")
    return targets


targets = {}  # {city: [population, gold]}
cities_input = input().split('||')

while cities_input[0] != 'Sail':

    city = cities_input[0]
    population = int(cities_input[1])
    gold = int(cities_input[2])
    if city not in targets:
        targets[city] = [population, gold]
    else:
        targets[city][0] += population
        targets[city][1] += gold
    cities_input = input().split('||')

events = input().split('=>')  # Plunder {town: [n_people, gold_q]}
                              # Prosper {town: gold_q}
while events[0] != 'End':
    town = events[1]
    if events[0] == 'Plunder':
        n_people = int(events[2])
        gold_q = int(events[3])
        targets = plunder(targets, town, n_people, gold_q)
    elif events[0] == 'Prosper':
        gold_q = int(events[2])
        if gold_q > 0:
            targets = prosper(targets, town, gold_q)
        else:
            print("Gold added cannot be a negative number!")
    events = input().split('=>')

counter = len(targets)

if targets:
    print(f"Ahoy, Captain! There are {counter} wealthy settlements to go to:")
    for location in targets:
        print(f"{location} -> Population: {targets[location][0]} citizens, Gold: {targets[location][1]} kg")

else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
