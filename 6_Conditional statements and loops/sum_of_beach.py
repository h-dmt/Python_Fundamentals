# Beaches are filled with sand, water, fish, and sun. Given a string,
# calculate how many times the words "Sand", "Water", "Fish", and "Sun"
# appear (case insensitive).

input_string = str(input())
input_string = input_string.lower()
counter = 0
list_words = ["water", "fish", "sun", "sand"]
for key in list_words:
    for j in range(0, len(input_string)):
        k = j + len(key)
        if k > len(input_string):
            k = len(input_string)
        if key in input_string[j:k]:
            counter += 1
print(counter)
