"""
You will receive a single integer - the number of electrons.
Your task is to fill shells until there are no more electrons left.
The rules for electron distribution are as follows:
    • The maximum number of electrons in a shell can be 2n2, where n is the
    position of a shell (starting from 1).
    For example, the maximum number of electrons in the 3rd shield can be 2*32 = 18.
    • You should start filling the shells from the first one at the first position.
    • If the electrons are enough to fill the first shell, the left unoccupied
    electrons should fill the following shell and so on.
In the end, print a list with the filled shells.
"""


def check_level_e(p, e):
    if e >= 2 * p**2:
        return 2 * p**2
    else:
        return False


filled_shells = []
electrons = int(input())
n = 0
while electrons > 0:
    n += 1
    if check_level_e(n, electrons):
        filled_shells.append(check_level_e(n, electrons))
        electrons -= filled_shells[-1]
    else:
        filled_shells.append(electrons)
        break
print(filled_shells)
