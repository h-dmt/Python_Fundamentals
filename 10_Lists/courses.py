"""
On the first line, you will receive a single number n.
On the following n lines, you will receive names of courses.
You should create a list of courses and print it.
"""

num_courses = int(input())
courses_str = []
for i in range(num_courses):
    courses_str.append(input())
print(courses_str)
