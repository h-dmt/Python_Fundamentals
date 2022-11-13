"""
Create a program that receives two strings on a single line separated by a single
space. Then, it prints the sum of their multiplied character codes as follows:
multiply str1[0] with str2[0] and add the result to the total sum,
then continue with the next two characters. If one of the strings is longer than
the other, add the remaining character codes to the total sum
without multiplication.
"""


def char_to_num(word):
    str_n = [ord(i) for i in word]
    return str_n


words = input().split()
w1_ascii = char_to_num(words[0])
w2_ascii = char_to_num(words[1])
tot = 0
a = 'a'
if len(w1_ascii) <= len(w2_ascii):
    shortest = w1_ascii
    longest = w2_ascii
else:
    shortest = w2_ascii
    longest = w1_ascii
tot = [shortest[x] * longest[x] for x in range(len(shortest))]
tot += longest[len(shortest):]
tot = sum(tot)
print(tot)
