"""
On the first line, you will receive a single number n.
On the following n lines, you will receive integers.
After that, you will be given one of the following commands:
    • even
    • odd
    • negative
    • positive
Filter all the numbers that fit in the category
(0 counts as a positive and even). Finally, print the result.
"""

n_ints = int(input())
lst_num = []
lst_filtered = []
is_even = 'even'
is_odd = 'odd'
is_negative = 'negative'
is_positive = 'positive'
for _ in range(n_ints):
    lst_num.append(int(input()))
type_filter = str(input())

for j in lst_num:
    apply_filter = (
            (type_filter == is_even and j % 2 == 0) or
            (type_filter == is_odd and j % 2 != 0) or
            (type_filter == is_negative and j < 0) or
            (type_filter == is_positive and j >= 0))
    if apply_filter:
        lst_filtered.append(j)
print(lst_filtered)
