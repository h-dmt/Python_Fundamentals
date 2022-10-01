"""
You will receive 2 lines of input. On the first line, you will receive a single
string of integers, separated by a comma and a space ", ".
On the second line, you will receive a count of beggars.
Your job is to print a list with the sum of what each beggar brings home,
assuming they all take regular turns, from the first to the last number in
the list.
For example: [1, 2, 3, 4, 5] for 2 beggars will return a result of 9 and 6,
as the first one takes [1, 3, 5], the second one collects [2, 4].
The same list with 3 beggars would produce a better outcome for the second beggar:
5, 7 and 3, as they will respectively take [1, 4], [2, 5], and [3].
Also, note that not all beggars have to take the same amount of "offers",
meaning that the length of the list is not necessarily a multiple of n.
The list length could be even shorter - i.e.,
the last beggars will take nothing (0).
"""
sales = str(input())
lst_sales = sales.split(', ')
beggers = int(input())
lst_begger_incomes = []
for i in range(beggers):
    lst_begger_incomes.append(0)

for j in range(beggers):
    for k in range(j, len(lst_sales), beggers):
        lst_begger_incomes[j] += int(lst_sales[k])

print(lst_begger_incomes)

