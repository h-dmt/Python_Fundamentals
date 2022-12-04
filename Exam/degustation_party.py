

guest_record = {}
disliked = 0

commands = input().split('-')
while commands[0] != 'Stop':
    guest, meal = commands[1:]
    if commands[0] == 'Like':
        if guest not in guest_record:
            guest_record[guest] = [meal]
        elif meal not in guest_record[guest]:
            guest_record[guest].append(meal)

    elif commands[0] == 'Dislike':
        if guest not in guest_record:
            print(f"{guest} is not at the party.")
        elif meal not in guest_record[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            guest_record[guest].remove(meal)
            disliked += 1
            print(f"{guest} doesn't like the {meal}.")

    commands = input().split('-')

for client in guest_record:
    print(f"{client}: {', '.join(guest_record[client])}")

print(f"Unliked meals: {disliked}")
