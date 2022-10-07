"""
Write a program that announces the winner of a car race.
You will receive a sequence of numbers. Each number represents the time the car
needs to pass through that step (the index).
There will be two cars. The first one starts from the left side, and the other one
starts from the right side. The middle index of the sequence is the finish line.
Calculate the total time each racer needs to reach the finish line and print the
winner with his total time (the racer with less time).
If you have a zero in the list, you should reduce the racer's time that reached it
by 20% (from his current time).
The number of elements in the sequence will always be odd.
Print the result in the following format
"The winner is {left/right} with total time: {total_time}".
The time should be formatted to the first decimal point.
"""

lst_times = str(input()).split()
lst_L = []
lst_R = []
t_L = 0
t_R = 0
winner = ''
win_time = 0

for i in range(0, (len(lst_times) - 1)//2):
    lst_L.append(lst_times[i])
    t_L += int(lst_times[i])
    if int(lst_times[i]) == 0:
        t_L *= 0.8
for j in range(len(lst_times) - 1, (len(lst_times) - 1) // 2, -1):
    lst_R.append(lst_times[j])
    t_R += int(lst_times[j])
    if int(lst_times[j]) == 0:
        t_R *= 0.8
if t_L < t_R:
    winner = 'left'
    win_time = t_L
else:
    winner = 'right'
    win_time = t_R

print(f'The winner is {winner} with total time: {win_time:.1f}')

