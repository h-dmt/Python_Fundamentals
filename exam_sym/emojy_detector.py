"""
    https://judge.softuni.org/Contests/Practice/Index/2302#1

    You have to get your cool threshold. It is obtained by multiplying all the digits
    found in the input.  The cool threshold could be a huge number, so be mindful.
An emoji is valid when:
    • It is surrounded by 2 characters, either "::" or "**"
    • It is at least 3 characters long (without the surrounding symbols)
    • It starts with a capital letter
    • Continues with lowercase letters only

Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::

You need to count all valid emojis in the text and calculate their coolness.
The coolness of the emoji is determined by summing all the ASCII values of all
letters in the emoji.
Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
"""
import re

some_text = input()
coolThresholdSum = 1
for character in some_text:
    if character.isdecimal():
        coolThresholdSum *= int(character)

emojy_pattern = r"(\:\:|\*\*)([A-Z][a-z]{2,})\1"
matches = re.findall(emojy_pattern, some_text)
emoji_list = []
emoji_coolnes = 0
boundary = ''
count = 0
for emoji in matches:
    for j in emoji[1]:
        emoji_coolnes += ord(j)  # count emojy coolness
    count += 1
    if emoji_coolnes >= coolThresholdSum:  # check if emojis character ascii sum is higher than cool threshold sum
        boundary = emoji[0]
        entire_emojy = boundary + emoji[1] + boundary
        emoji_list.append(entire_emojy)
    emoji_coolnes = 0

print(f"Cool threshold: {coolThresholdSum}")
print(f"{count} emojis found in the text. The cool ones are:")
for i in emoji_list:
    print(i)
