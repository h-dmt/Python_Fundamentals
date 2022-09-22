# Calculate how many courses will be needed to elevate N persons
# by using an elevator with a capacity of P persons.
# The input holds two lines: the number of people N and the capacity P of the elevator.

n_person = int(input())
capacity = int(input())
if n_person % capacity == 0:
    courses = int(n_person / capacity)
else:
    courses = int(n_person // capacity + 1)
print(courses)
