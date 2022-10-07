"""
Write a program that receives a single string
(integers separated by a comma and space ", "),
finds all the zeros, and moves them to the back without messing up the other elements.
Print the resulting integer list.
"""
num_list = str(input()).split(', ')
zeros_back = []

for i in num_list:
    if int(i) != 0:
        zeros_back.append(int(i))
while len(zeros_back) != len(num_list):
    zeros_back.append(0)
print(zeros_back)
