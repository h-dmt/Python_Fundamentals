"""
You will be given the coordinates of four points.
The first and the second pair of points form two different lines.

Create a function that prints the longer line in the format
"({X1}, {Y1})({X2}, {Y2})" starting from the point which is closer to
the center of the coordinate system (0, 0).

If the lines are of equal length, print only the first one.
The resulting coordinates must be formatted to the lower integer.
"""
import math


def origin_dist(x_1, y_1, x_2, y_2):
    if (x_1**2 + y_1**2)**0.5 <= (x_2**2 + y_2**2)**0.5:
        # Point 1 nearest to origin
        return f"({math.floor(x_1)}, {math.floor(y_1)})" \
               f"({math.floor(x_2)}, {math.floor(y_2)})"
    else:
        # Point 2 nearest to origin
        return f"({math.floor(x_2)}, {math.floor(y_2)})" \
               f"({math.floor(x_1)}, {math.floor(y_1)})"


def line_length(dx, dy):
    return (dx**2 + dy**2)**0.5


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
dx_1 = abs(x2 - x1)
dy_1 = abs(y2 - y1)
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
dx_2 = abs(x4 - x3)
dy_2 = abs(y4 - y3)

# Determine the longest line
if line_length(dx_1, dy_1) >= line_length(dx_2, dy_2):
    print(origin_dist(x1, y1, x2, y2))
else:
    print(origin_dist(x3, y3, x4, y4))
