"""
You will be given the coordinates of two points on a Cartesian coordinate system
 - X1, Y1, X2, and Y2 on separate lines.
 Write a function that prints the point which is closest to the center of the
 coordinate system (0, 0) in the format: "({X}, {Y})"
If the points are at the same distance from the center, print only the first one.
The resulting coordinates must be formatted to the lower integer.
"""
import math


def smallest_dist(x_1, y_1, x_2, y_2):

    p1_d = abs(x_1) + abs(y_1)
    p2_d = abs(x_2) + abs(y_2)
    if p1_d <= p2_d:
        return f"({math.floor(x_1)}, {math.floor(y_1)})"
    else:
        return f"({math.floor(x_2)}, {math.floor(y_2)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(smallest_dist(x1, y1, x2, y2))

