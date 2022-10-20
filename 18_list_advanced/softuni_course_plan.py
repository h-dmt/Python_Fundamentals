"""
The possible commands are:
    • "Add:{lessonTitle}" - add the lesson to the end of the schedule
        if it does not exist.
    • "Insert:{lessonTitle}:{index}" - insert the lesson to the given index,
        if it does not exist.
    • "Remove:{lessonTitle}" - remove the lesson, if it exists.
    • "Swap:{lessonTitle}:{lessonTitle}" - swap the position of the two lessons
        if they exist.
    • "Exercise:{lessonTitle}" - add Exercise in the schedule right after the
        lesson index, if the lesson exists and there is no exercise already,
        in the following format "{lessonTitle}-Exercise".
        If the lesson doesn't exist, add the lesson at the end of the course
        schedule, followed by the Exercise.
"""

# Each time you Swap or Remove a lesson,
# you should do the same with the Exercises,
# if there are any following the lessons.


def add_exercise(lesson, lst_lect):
#  add Exercise in the schedule right after the lesson index,
#  if the lesson exists and there is no exercise already, in the following format
#  "{lessonTitle}-Exercise"

# If the lesson doesn't exist, add the lesson at the end of the course schedule,
# followed by the Exercise.

    exercise_lect = lesson + '-' + 'Exercise'
    if lesson in lst_lect and exercise_lect not in lst_lect:
        exercise_lect = lesson + '-' + 'Exercise'
        lesson_index = lst_lect.index(lesson)
        lst_lect.insert(lesson_index + 1, exercise_lect)
    elif lesson not in lst_lect:
        lst_lect.append(lesson)
        lst_lect.append(exercise_lect)
    return lst_lect


def swap_lessons(lect_1, lect_2, lst_lect):

    if lect_1 in lst_lect and lect_2 in lst_lect:
        index_1 = lst_lect.index(lect_1)
        index_2 = lst_lect.index(lect_2)
        exe_1 = lect_1 + '-' + 'Exercise'
        exe_2 = lect_2 + '-' + 'Exercise'
        lst_lect[index_1] = lect_2
        lst_lect[index_2] = lect_1
        if exe_2 in lst_lect:
            lst_lect.remove(exe_2)
            index_2 = lst_lect.index(lect_2)
            lst_lect.insert(index_2 + 1, exe_2)

        if exe_1 in lst_lect:
            lst_lect.remove(exe_1)
            index_1 = lst_lect.index(lect_1)
            lst_lect.insert(index_1 + 1, exe_1)

    return lst_lect


def remove_course(lecture, lst_lect):
    exe = lecture + '-' + 'Exercise'
    if lecture in lst_lect:
        lst_lect.remove(lecture)
        if exe in lst_lect:
            lst_lect.remove(exe)

    return lst_lect


course_lst = input().split(', ')
command = input()
if 'start' in command:
    command = command.split()
else:
    command = command.split(':')

while command[1] != 'start':

    if command[0] == 'Add':
        if command[1] not in course_lst:
            course_lst.append(command[1])

    elif command[0] == 'Insert':
        index = int(command[2])
        if command[1] not in course_lst:
            course_lst.insert(index, command[1])

    elif command[0] == 'Remove':
        lesson = command[1]
        course_lst = remove_course(lesson, course_lst)

    elif command[0] == 'Swap':
        lesson_1 = command[1]
        lesson_2 = command[2]
        course_lst = swap_lessons(lesson_1, lesson_2, course_lst)

    elif command[0] == 'Exercise':
        exercise = command[1]
        course_lst = add_exercise(exercise, course_lst)
    #print(course_lst)
    command = input()
    if 'start' in command:
        command = command.split()
    else:
        command = command.split(':')

for i in course_lst:
    print(course_lst.index(i) + 1, end='')
    print(f".{i}")
