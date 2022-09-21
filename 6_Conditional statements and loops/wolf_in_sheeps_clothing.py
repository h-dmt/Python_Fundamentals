"""
Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing
at the front of the queue, which is at the end of the list:
[sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
   4      3            2      1
If the wolf is the closest animal to you, print "Please go away and stop eating my sheep".
Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!"
where N is the sheep's position in the queue.
Note: there will always be exactly one wolf on the list.
"""

sheep_queue = str(input())
position_wolf = 0
wolf = ''
elements = 0

for i in range(len(sheep_queue)):
    if sheep_queue[i] == 's':
        elements += 1
    elif sheep_queue[i] == 'w':
        position_wolf = elements + 1
elements += 1
# print(f'sheeps = {elements - 1}')
# print(f'position wolf = {position_wolf}')

if position_wolf == elements:
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {elements - position_wolf}! You are about to be eaten by a wolf!')
