"""
You will receive two lines of input:
    • a list of employees' happiness as a string of numbers separated
    by a single space
    • a happiness improvement factor (single number).
Your task is to find out if the employees are generally happy in their office.
First, multiply each employee's happiness by the factor.
Then, print one of the following lines:
    • If half or more of the employees have happiness greater than or equal
    to the average:
"Score: {happy_count}/{total_count}. Employees are happy!"
    • Otherwise:
"Score: {happy_count}/{total_count}. Employees are not happy!"
"""

happines = list(map(int, input().split()))
factor = int(input())
happines = [i * factor for i in happines]
total_count = len(happines)
avg_happines = sum(happines) / total_count

happy_count = list(filter(lambda k: k >= avg_happines, happines))
# print(happines)
# print(happy_count)

if len(happy_count) >= len(happines) / 2:
    print(f"Score: {len(happy_count)}/{total_count}. Employees are happy!")
else:
    print(f"Score: {len(happy_count)}/{total_count}. Employees are not happy!")
