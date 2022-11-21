"""
reads N lines of strings and extracts the name and the age of a given person:
    • The person's name will be surrounded by "@" and "|" in the format "@{name}|".
    • The person's age will be surrounded by "#" and "*" in the format "#{age}*".
Example: "Hello my name is @Peter| and I am #20* years old."
For each found name-age pair, print a line in the following format
"{name} is {age} years old."
"""

import re
n = int(input())
for _ in range(n):
    some_text = input()
    name_pattern = r"\@(\w+)\|"
    age_pattern = r"\#(\d+)\*"
    name = re.findall(name_pattern, some_text)
    age = re.findall(age_pattern, some_text)
    print(f"{name[0]} is {age[0]} years old.")
