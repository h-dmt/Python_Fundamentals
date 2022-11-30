# https://judge.softuni.org/Contests/Practice/Index/2518#0
# 25-11-22


def add_stop(stops, indx, add_str):
    if 0 <= indx < len(stops):
        stops = stops[:indx] + add_str + stops[indx:]
    return stops


def remove_stop(start_ind, end_ind, stops):
    if 0 <= start_ind <= end_ind < len(stops):
        stops = stops[:start_ind] + stops[end_ind+1:]
    return stops


stops = input()
command_input = input().split(':')


while True:
    if command_input[0] == 'Travel':
        break
    elif command_input[0] == 'Add Stop':
        index = int(command_input[1])
        str_add = command_input[2]
        stops = add_stop(stops, index, str_add)

    elif command_input[0] == 'Remove Stop':
        ind_1 = int(command_input[1])
        ind_2 = int(command_input[2])
        stops = remove_stop(ind_1, ind_2, stops)

    elif command_input[0] == 'Switch':
        old = command_input[1]
        new = command_input[2]
        if old in stops:
            stops = stops.replace(old, new)
    print(stops)
    command_input = input().split(':')
print(f"Ready for world tour! Planned stops: {stops}")
