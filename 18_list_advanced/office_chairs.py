"""
On the first line, you will be given an integer n representing the number of rooms
in the business center. On the following n lines for each room, you will receive
information about the chairs in the room and the number of visitors.
Each chair will be presented with the char "X". Next, there will be a single space
and the number of visitors at the end.
For example: "XXXXX 4" (5 chairs and 4 visitors).
Keep track of the free chairs:
    • If there are not enough chairs in a specific room, print the following message:
     "{needed_chairs_in_room} more chairs needed in room {number_of_room}".
     The rooms start from 1.
    • Otherwise, print: "Game On, {total_free_chairs} free chairs left".
"""


def free_chairs(n_chairs, n_guest):
    free_chairs = 0
    if len(n_chairs) >= int(n_guest):
        free_chairs += len(n_chairs) - int(n_guest)
    return free_chairs


num_rooms = int(input())
room_chair_lst = []
tot_free_chairs = 0
tot_guests = 0
needs = []
for room in range(num_rooms):
    chairs, guests = (input().split())
    tot_guests += int(guests)
    tot_free_chairs += len(chairs)
    if not free_chairs(chairs, guests):
        needed_ch = int(guests) - len(chairs)
        needs.append([needed_ch, room + 1])

if tot_free_chairs >= tot_guests:
    print(f"Game On, {tot_free_chairs - tot_guests} free chairs left")
else:
    for i in range(len(needs)):
        print(f"{needs[i][0]} more chairs needed in room {needs[i][1]}")

"""    
if free_chairs >= needed_chairs:
    print(f"{needed_chairs_in_room} more chairs needed in room {number_of_room}")
"""