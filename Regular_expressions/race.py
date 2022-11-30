"""
    On the first line you will be given list of participants separated by ", "
    On the next few lines until you receive a line "end of race" you will be
    given some info which will be some alphanumeric characters.
    For example: "G!32e%o7r#32g$235@!2e". The letters are the name of the person and
    the sum of the digits is the distance he ran.
    So here we have George who ran 29 km.
    Store the information about the person only if the list of racers contains the
    name of the person.
    If you receive the same person more than once just add the distance to
    his old distance.
    At the end print the top 3 racers ordered by distance in descending in the format:
    "1st place: {first racer}
     2nd place: {second racer}
     3rd place: {third racer}"
"""
import re

name_pattern = r'[A-Za-z]+'
distance_pattern = r'\d'
participants = input().split(', ')
name_distance = input()
record = {}
while name_distance != 'end of race':
    name = ''.join(re.findall(name_pattern, name_distance))
    distance = list(map(int, re.findall(distance_pattern, name_distance)))
    distance = sum(distance)
    if name in participants:
        if name not in record:
            record[name] = distance
        else:
            record[name] += distance
    name_distance = input()

record = sorted(record.items(), key=lambda i: -i[1])

print(f"1st place: {record[0][0]}\n"
      f"2nd place: {record[1][0]}\n"
      f"3rd place: {record[2][0]}")
