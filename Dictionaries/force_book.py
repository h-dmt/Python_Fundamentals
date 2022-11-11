"""
You will receive several input lines in one of the following formats:
"{force_side} | {force_user}"
"{force_user} -> {force_side}"

If you receive "force_side | force_user":
    • If there is no such force user and no such force side -> create a new force
        side and add the force user to the corresponding side.
    • Only if there is no such force user in any force side -> add the force user
        to the corresponding side.
    • If there is such force user already -> skip the command and continue to the
        next operation.
If you receive a "force_user -> force_side":
    • If there is such force user already -> change their side.
    • If there is no such force user in any force side -> add the force user to the
        corresponding force side.
    • If there is no such force user and no such force side -> create new force side
        and add the force user to the corresponding side.
    • Then you should print on the console: "{force_user} joins the {force_side}
        side!".
You should end your program when you receive the command "Lumpawaroo".
"""


class ForceBook:
    def __init__(self):
        self.force_side = {}

    def join(self, usr: str, side: str):
        # check if Light
        if [usr] not in self.force_side.values():
            if side in self.force_side.keys():
                self.force_side[side].append(usr)
            else:
                self.force_side[side] = [usr]

    def switch(self, usr: str, side: str):
        # if user not in any of the forces
        if [usr] not in self.force_side.values():
            # if the side exists
            if side in self.force_side.keys():
                self.force_side[side].append(usr)
                print(f"{usr} joins the {side} side!")
            else:  # if side doesn't exist
                self.force_side[side] = [usr]
                print(f"{usr} joins the {side} side!")
        # if user already in one of the forces
        else:
            k_remove = [k for k, v in self.force_side.items() if v == [usr]]
            self.force_side[k_remove[0]].remove(usr)  # remove user from side
            # if the side exists
            if side in self.force_side.keys():
                self.force_side[side].append(usr)
                print(f"{usr} joins the {side} side!")
            else:  # if side doesn't exist
                self.force_side[side] = [usr]
                print(f"{usr} joins the {side} side!")


force_book = ForceBook()
user_input = input()
if '->' in user_input:
    user_input = user_input.split(' -> ')
    user_input.append('->')
elif '|' in user_input:
    user_input = user_input.split(' | ')
    user_input.append('|')
else:
    user_input.split()

while user_input != "Lumpawaroo":
    # Switch to other Force
    if user_input[2] == '->':
        force = user_input[1]
        name = user_input[0]
        force_book.switch(name, force)
    # Join Force
    elif user_input[2] == '|':
        force = user_input[0]
        name = user_input[1]
        force_book.join(name, force)

    user_input = input()
    if '->' in user_input:
        user_input = user_input.split(' -> ')
        user_input.append('->')
    elif '|' in user_input:
        user_input = user_input.split(' | ')
        user_input.append('|')
    else:
        user_input.split()

# Printing the Force Book
for side_f in force_book.force_side:
    if len(force_book.force_side[side_f]) > 0:
        num_fighters = len(force_book.force_side[side_f])
        print(f"Side: {side_f}, Members: {num_fighters}")
        for fighters in force_book.force_side[side_f]:
            print(f"! {fighters}")
