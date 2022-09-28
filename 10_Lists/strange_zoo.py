"""
    You will receive 3 strings on separate lines, representing the
    tail, the body, and the head of an animal in that order.
    Your task is to re-arrange the elements in a list so that the animal looks
    normal again:
    • On the first position is the head;
    • On the second position is the body;
    • On the last one is the tail.
"""

input_str = []
for i in range(3):
    input_str.append(input())
input_str[0],  input_str[2] = input_str[2], input_str[0]
print(input_str)
