"""
Given a number n representing the number of rows of a board of dots and dashes.
On the following n lines, you will receive each row of the board as a string with
symbols (dots and dashes only), separated by a single space.
Your task is to find and print the largest count of dots that could be connected at
once. You could only connect horizontally or vertically.
"""


def split_rows(table, r):
    roww = table[r].split()
    return roww


def count_dots(in_row):
    indx = []
    indx_old = []
    max_dot = 0
    count = 0
    for i in range(len(in_row)):
        if in_row[i] == '.':
            count += 1
            indx.append(i)
    return count, indx


def check_indexes(id_list, id_m):
    rws = len(id_list)
    n = 0
    row_max = id_list[id_m]
    # if row with max dots is on top
    if id_m == 0:
        for ind1 in range(id_m+1, rws):
            next_row = id_list[ind1]
            for p in range(len(next_row)):
                if next_row[p] == row_max[p]:
                    n += 1
                    n_next = check_around(next_row, next_row[p])
                    n += n_next
                    row_max = next_row
    # if row with max dots is last
    elif id_m == rws:
        row_max = id_list[id_m]
        for ind2 in range(rws-1, -1, -1):
            next_row = id_list[ind2]
            for p2 in range(len(next_row)):
                if next_row[p2] == row_max[p2]:
                    n += 1
                    n_next = check_around(next_row, next_row[p2])
                    n += n_next
                    row_max = next_row
    # if row with max dots is in the middle
    # check first upwards
    elif 0 < id_m < rws:
        row_max = id_list[id_m]
        for ind3 in range(id_m+1, rws):
            next_row = id_list[ind3]
            for p3 in range(len(next_row)):
                if next_row[p3] == row_max[p3]:
                    n += 1
                    n_next = check_around(next_row, next_row[p3])
                    n += n_next
                    row_max = next_row
        # then downwards
        row_max = id_list[id_m]
        for ind4 in range(rws-1, -1, -1):
            next_row = id_list[ind4]
            for p4 in range(len(next_row)):
                if next_row[p4] == row_max[p4]:
                    n += 1
                    n_next = check_around(next_row, next_row[p4])
                    n += n_next
                    row_max = next_row
    return n


def check_around(row, id):  # check if indexes in row from id are a sequence
    num = 0
    l = len(row)
    print(row)
    print(id)
    if id == 0:
        for a in range(id+1, l+1):
            if row[a] == a:
                num += 1
    elif id == l:
        for b in range(id-1, -1, -1):
            if row[b] == b:
                num += 1
    else:
        for c in range(id+1, l):
            if row[c] == c:
                num += 1
        for d in range(id, -1, -1):
            if row[d] == d:
                num += 1
    return num


n = int(input())
rows = []
dots_per_row = []
indexes_per_row = []
count = 0
max_per_row = 0
row_max_dots = 0
for _ in range(n):
    rows.append(input())
for r in range(len(rows)):
    row = split_rows(rows, r)
    dots, d_indx = count_dots(row)  # count dots and indexes per every row
    dots_per_row.append(dots)  # dots on every row
    indexes_per_row.append(d_indx)  # indexes on every row
    if len(d_indx) > max_per_row:
        max_per_row = len(d_indx)
        row_max_dots = r
united_dots = check_indexes(indexes_per_row, row_max_dots)
print(united_dots)
# print(dots_per_row)
print(indexes_per_row)
