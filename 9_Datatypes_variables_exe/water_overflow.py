# You have a water tank with a capacity of 255 liters.
# On the first line, you will receive n – the number of lines,
# which will follow. On the following n lines, you will receive liters of water
# (integers), which you should pour into your tank.
# If the capacity is not enough, print "Insufficient capacity!"
# and continue reading the next line. On the last line,
# print the liters in the tank.

n_lines = int(input())
capacity = 255
current_level = 0
line_flow = 0
for _ in range(n_lines):
    line_flow = int(input())
    current_level += line_flow
    if current_level > capacity:
        current_level -= line_flow
        print('Insufficient capacity!')
print(f'{current_level}')
