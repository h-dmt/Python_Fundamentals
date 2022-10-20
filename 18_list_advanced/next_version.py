"""
You will be given a string representing the version of your software in the format:
"{n1}.{n2}.{n3}". Your task is to print the next version. For example, if the current
version is "1.3.4", the next version will be "1.3.5".
The only rule is that the numbers cannot be greater than 9. If it happens,
set the current number to 0 and increase the previous number. For more clarification,
see the examples below.
Note: there will be no case in which the first number will become greater than 9.
"""

version_current = input().split('.')
version_current = list(map(int, version_current))
next_version = version_current[:]
if version_current[-1] < 9:
    next_version[-1] += 1
elif version_current[-1] == 9:
    next_version[-1] = 0
    if version_current[-2] < 9:
        next_version[-2] += 1
    elif version_current[-2] == 9:
        next_version[-2] = 0
        next_version[0] += 1
print(*next_version, sep='.')


