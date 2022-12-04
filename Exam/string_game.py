

def change(the_string, chars, new_one):
    the_string = the_string.replace(chars, new_one)
    return the_string


def cut_str(the_string, start_i, k):
    if start_i + k < len(the_string):
        new_string = the_string[start_i:start_i + k]
    else:
        new_string = the_string[start_i:]
    cutted = the_string.replace(new_string, '')
    #print(cutted)
    return new_string


some_str = input()
while True:
    commands = input().split(' ')
    if commands[0] == 'Done':
        break
    else:
        if commands[0] == 'Change':
            some_str = change(some_str, commands[1], commands[2])
            print(some_str)
        elif commands[0] == 'Includes':
            if commands[1] in some_str:
                print(True)
            else:
                print(False)
        elif commands[0] == 'End':
            if some_str.endswith(commands[1]):
                print(True)
            else:
                print(False)
        elif commands[0] == "Uppercase":
            some_str = some_str.upper()
            print(some_str)
        elif commands[0] == 'FindIndex':
            letter = commands[1]
            if letter in some_str:
                index = some_str.index(letter)
                print(index)
        elif commands[0] == 'Cut':
            start_index = int(commands[1])
            counter = int(commands[2])
            if 0 <= start_index < len(some_str):
                some_str = cut_str(some_str, start_index, counter)
                print(some_str)