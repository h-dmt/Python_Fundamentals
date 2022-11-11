"""
Write a program that keeps the information about students and their grades.
On the first line, you will receive an integer number representing the next pair
of rows. On the next lines, you will be receiving each student's name and their
grade.
Keep track of all grades for each student and keep only the students with an
average grade higher than or equal to 4.50.
Print the final dictionary with students and their average grade in the
following format:
"{name} -> {averageGrade}"
Format the average grade to the 2nd decimal place.
"""


def check_grades(dct):
    for student in dct:
        if dct[student] < 4.50:
            del student
    return dct


def find_average(dct_g):
    averages = {}
    for std in dct_g:
        average_std = sum(dct_g[std]) / len(dct_g[std])
        if average_std >= 4.50:
            averages[std] = average_std
    return averages


n = int(input())
student_grades = {}
for _ in range(n):
    name = input()
    grade = [float(input())]
    if name in student_grades:
        student_grades[name].append(grade[0])
    else:
        student_grades[name] = grade

student_average = find_average(student_grades)
student_pass = check_grades(student_average)
for stud in student_pass:
    print(f"{stud} -> {student_pass[stud]:.2f}")
