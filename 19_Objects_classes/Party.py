"""
Create a class Party that only has an attribute people – empty list.
The __init__ method should not accept any parameters.
You will be given names of people (on separate lines)
until you receive the command "End". Use the created class to solve this problem.
After you receive the "End" command, print 2 lines:
    • "Going: {people}" - the people should be separated by comma and space ", ".
    • "Total: {total_people_going}"
"""


class Party:
    def __init__(self):
        self.people = list()


comand = input()
party = Party()  # Create instance
while comand != 'End':
    party.people.append(comand)
    comand = input()

n_people = len(party.people)
party.people = ', '.join(party.people)
print(f"Going: {party.people}")
print(f"Total: {n_people}")
