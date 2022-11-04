"""
You will be receiving names of students, their ID, and a course of programming
they have taken in the format "{name}:{ID}:{course}".
On the last line, you will receive a name of a course in snake case lowercase
letters. You should print only the information of the students who have taken the
corresponding course in the format: "{name} - {ID}" on separate lines.
"""


students_course = {}
str_in = input().split(':')
while len(str_in) > 1:
    course = str_in[2].replace(' ', '_')
    student = str_in[0] + ' '+'-'+' ' + str_in[1]
    students_course.update({student: course})
    str_in = input().split(':')
target = str_in[0].replace(' ', '_')

for stud in students_course:
    if students_course[stud] == target:
        print(stud)
