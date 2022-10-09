"""
Write a function that receives a string and a counter n.
The function should return a new string – the result of repeating the old string
n times. Print the result of the function. Try using lambda.
"""


str_in = input()
n = int(input())
str_out = lambda x, a_string: x * a_string
print(str_out(n, str_in))


