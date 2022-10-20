"""
You will receive a sequence of integers, separated by spaces -
the distances to the pokemon. Then you will begin receiving integers,
which will correspond to indexes in that sequence.
When you receive an index, you must remove the element at that index from
the sequence (as if you've captured the pokemon).
    • You must increase the value of all elements in the sequence which are
    less or equal to the removed element with the value of the removed element.
    • You must decrease the value of all elements in the sequence which are
    greater than the removed element with the value of the removed element.
If the given index is less than 0, remove the first element of the sequence,
and copy the last element to its place.
If the given index is greater than the last index of the sequence,
remove the last element from the sequence, and copy the first element to its place.
The increasing and decreasing elements should also be done in these cases.
The element whose value you should use is the removed element.
The program ends when the sequence has no elements
(there are no pokemon left for Ely to catch).
"""


def rem_index(index, lst):
    lst = list(map(int, lst))
    # If the given index is less than 0, remove the first element of the sequence,
    # and copy the last element to its place
    if index < 0:
        rem_elem = lst[-1]
        del lst[0]
        lst.insert(0, rem_elem)
    # If the given index is greater than the last index of the sequence,
    # remove the last element from the sequence, and copy the first element
    # to its place.
    elif index >= len(lst):
        rem_elem = lst[0]
        del lst[-1]
        lst.append(rem_elem)
    else:
        # remove the element at that index from the sequence
        rem_elem = lst[index]
        del lst[index]

    for i in range(len(lst)):
        if lst[i] <= rem_elem:
            # increase the value of all elements in the sequence
            # which are less or equal to the removed element with the value of
            # the removed element.
            lst[i] += rem_elem
        elif lst[i] > rem_elem:
            lst[i] -= rem_elem
    return lst, rem_elem


pokemons = input().split()
removed = 0
del_elem = 0
while len(pokemons) > 0:
    ind = int(input())
    pokemons, del_elem = rem_index(ind, pokemons)
    removed += del_elem
    print(*pokemons, sep=' ')

print(removed)
