"""
You will receive a field of a tic-tac-toe game in three lines containing numbers,
separated by a single space.
Legend:
    • 0 - empty space
    • 1 - first player move
    • 2 - second player move
Find out who the winner is. If the first player wins, print "First player won".
If the second player wins, print "Second player won". Otherwise, print "Draw!".
"""
row_1 = str(input()).split()
row_2 = str(input()).split()
row_3 = str(input()).split()

winner = 0

for i in range(len(row_3)):
    # vertical tris
    if row_1[i] == row_2[i] == row_3[i]:
        winner = row_3[i]
# vertical tris
if row_3[0] == row_3[1] == row_3[2]:
    winner = row_3[0]
elif row_2[0] == row_2[1] == row_2[2]:
    winner = row_2[0]
elif row_1[0] == row_1[1] == row_1[2]:
    winner = row_1[0]

# diagonal tris
if row_1[0] == row_2[1] == row_3[2]:
    winner = row_1[0]
elif row_1[2] == row_2[1] == row_3[0]:
    winner = row_1[2]

# who wins

if int(winner) == 1:
    print('First player won')
elif int(winner) == 2:
    print('Second player won')
else:
    print('Draw!')
