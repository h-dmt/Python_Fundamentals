"""
Using comprehension, write a program that receives some text,
separated by space, and take only those words whose length is even.
Print each word on a new line.
"""

words = input().split()
filtered_words = [x for x in words if len(x) % 2 == 0]
for w in filtered_words:
    print(w)
