"""
Write a program that prints all elements from a given sequence of words that occur
an odd number of times (case-insensitive) in it.
    • Words are given on a single line, space-separated.
    • Print the result elements in lowercase, in their order of appearance.
"""

words = input().split(' ')
words_dct = {}
for word in words:
    word_lower = word.lower()
    if word_lower not in words_dct:
        words_dct[word_lower] = 0
    words_dct[word_lower] += 1

for key in words_dct:
    if words_dct[key] % 2 != 0:
        print(key, end=' ')
