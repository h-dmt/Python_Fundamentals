"""
On the first line, you will receive a number n. On the following n lines,
you will receive integers. You should create and print two lists:
    • One with all the positives (including 0) numbers
    • One with all the negatives numbers
Finally, print the following message:
"Count of positives: {count_positives}
Sum of negatives: {sum_of_negatives}"
"""
number_elements = int(input())
lst_positive = []
lst_negative = []
element = 0
sum_pos = 0
sum_neg = 0
for i in range(number_elements):
    element = int(input())
    if element >= 0:
        lst_positive.append(element)
        sum_pos += 1
    else:
        lst_negative.append(element)
        sum_neg += element
print(lst_positive)
print(lst_negative)
print(f'Count of positives: {sum_pos}')
print(f'Sum of negatives: {sum_neg}')
