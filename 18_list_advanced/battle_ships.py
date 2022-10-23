"""
You will be given a number n representing the number of rows of the field.
On the following n lines, you will receive each field row as a string with
numbers separated by a space. Each number greater than zero represents a ship
with health equal to the number value.
After that, you will receive the squares that are being attacked in the format:
 "{row}-{col} {row}-{col}".
Each time a square is being attacked, if there is a ship (number greater than 0),
you should reduce its value by 1. If a ship's health reaches zero,
it is destroyed. After the attacks have ended, print how many ships were destroyed.
"""


def strike(roww, pos):
    destroyed = False
    if roww[pos] > 0:
        roww[pos] -= 1
        if roww[pos] == 0:
            destroyed = True
    return roww, destroyed


rows_field = int(input())
battlefield = []
for i in range(rows_field):
    battlefield.append(list(map(int, input().split(' '))))
columns_field = len(battlefield[0])
attacks = input().split(' ')
sinked = False
count = 0
for k in attacks:
    row, column = map(int, k.split('-'))
    battlefield[row], sinked = strike(battlefield[row], column)
    if sinked:
        count += 1
print(count)
