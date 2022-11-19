import re
numbers = input()
# ["+359 2 222 2222", "359-2-222-2222", "+359/2/222/2222",
#            "+359-2 222 2222", "+359 2-222-2222", "+359-2-222-222", "+359-2-222-22222", "+359-2-222-2222"]

pattern = r"\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4}\b"
                              # ^ separated by line OR by ^ white space
matches = re.findall(pattern, numbers)
previous = ''
"""for match in matches:
    if match == previous:
        matches.remove(previous)
    previous = match"""
print(', '.join(matches))
