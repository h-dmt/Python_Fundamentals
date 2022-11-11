"""
You will be receiving a course name and a student name until you receive
the command "end".
You should register each user into the corresponding course.
If the given course does not exist, add it.
When you receive the command "end", print the courses with their names and total
registered users. For each course, print the registered users.

Input
    • Until the "end" command is received, you will be receiving input lines
    in the format:
    "{course_name} : {student_name}"
    • The product data is always delimited by " : "
Output
    • Print the information about each course in the following format:
    "{course_name}: {registered_students}"
    • Print the information about each student in the following format:
    "-- {student_name}"
"""


class CourseOrg:
    def __init__(self):
        self.courses = {}

    def add_student(self, name: str, to_course: str):
        if to_course not in self.courses:
            self.courses[to_course] = [name]
        else:
            self.courses[to_course].append(name)


data_input = input().split(' : ')
course = CourseOrg()
while data_input[0] != 'end':
    student_name = data_input[1]
    join_course = data_input[0]
    course.add_student(student_name, join_course)
    data_input = input().split(' : ')

for key_course in course.courses:
    n_students = len(course.courses[key_course])
    print(f"{key_course}: {n_students}")
    for n in range(len(course.courses[key_course])):
        stud = course.courses[key_course][n]
        print(f"-- {stud}")
