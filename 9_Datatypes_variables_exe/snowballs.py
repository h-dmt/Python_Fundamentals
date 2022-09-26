"""
You will receive N – an integer, the number of snowballs being made by
 Tony and Andi.
On the following lines, you will receive 3 inputs for each snowball:
    • The weight of the snowball (integer).
    • The time needed for the snowball to get to its target (integer).
    • The quality of the snowball (integer).
For each snowball, you must calculate its value by the following formula:

            (snowball_weight / snowball_time) ** snowball_quality

In the end, you must print the highest calculated value of a snowball.
"""
N = int(input())
ball_weight = []
ball_time = []
ball_quality = []
ball_index = []
best_ball = 0
best_quality = 0
best_time = 0
best_weight = 0
for i in range(N):
    ball_weight.append(int(input()))
    ball_time.append(int(input()))
    ball_quality.append(int(input()))
    ball_index.append((ball_weight[i] / ball_time[i]) ** ball_quality[i])
    if ball_index[i] > best_ball:
        best_ball = ball_index[i]
        best_quality = ball_quality[i]
        best_time = ball_time[i]
        best_weight = ball_weight[i]
print(f'{best_weight} : {best_time} = {int(best_ball)} ({best_quality})')
