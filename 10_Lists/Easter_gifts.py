"""
First, you are going to receive the gifts you plan on buying on a single line,
separated by space, in the following format:
"{gift1} {gift2} {gift3}… {giftn}"
Then you will start receiving commands until you read the "No Money" message.
There are three possible commands:
    • "OutOfStock {gift}"
        ◦ Find the gifts with this name in your collection, if any, and change
         their values to "None".
    • "Required {gift} {index}"
        ◦ If the index is valid, replace the gift on the given index with the given
        gift.
    • "JustInCase {gift}"
        ◦ Replace the value of your last gift with this one.
In the end, print the gifts on a single line, except the ones with value "None",
separated by a single space in the following format:
"{gift1} {gift2} {gift3} … {giftn}"
"""
plan_gifts = str(input()).split()
command = str(input()).split()
index = 0
no_money = ['No', 'Money']

while no_money != command:
    if 'OutOfStock' in command:
        for i in range(len(plan_gifts)):
            if plan_gifts[i] == command[1]:
                plan_gifts[i] = 'None'
    elif 'Required' in command:
        if len(command) == 3 and isinstance(int(command[2]), int):
            index = int(command[2])
        if 0 <= index < len(plan_gifts):
            plan_gifts[index] = command[1]
    elif 'JustInCase' in command:
        if len(plan_gifts) >= 1:
            plan_gifts[-1] = command[1]
        else:
            plan_gifts.append(command[1])
    command = str(input()).split()

while 'None' in plan_gifts:
    plan_gifts.remove('None')

print(' '.join(plan_gifts))
