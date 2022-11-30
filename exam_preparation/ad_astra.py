
 #  https://judge.softuni.org/Contests/Practice/Index/2525#1
#  24-11-22

import re

pattern = r"(\#|\|)([A-Za-z]+\s?[A-Za-z]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(\d+)\1"

message = input()
calories = 0
stuff = re.findall(pattern, message)
collection = []
for items in stuff:
    calories += int(items[3])
    item_name = items[1]
    expiration_date = items[2]
    collection.append([item_name, expiration_date, int(items[3])])
days = calories // 2000
print(f"You have food to last you for: {days} days!")
for food in collection:
    print(f"Item: {food[0]}, Best before: {food[1]}, Nutrition: {food[2]}")
