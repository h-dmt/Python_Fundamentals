"""
A faro shuffle is a method for shuffling a deck of cards, in which the deck
is split exactly in half. Then the cards in the two halves are
perfectly interleaved, such that the original bottom card is still on
the bottom and the original top card is still on top.
For example, faro shuffling the list
['ace', 'two', 'three', 'four', 'five', 'six'] once,gives
['ace', 'four', 'two', 'five', 'three', 'six']
Write a program that receives a single string (cards separated by space)
and on the second line receives a count of faro shuffles that should be made.
Print the state of the deck after the shuffle.
Note: The length of the deck of cards will always be an even number.
"""

str_in = str(input())
n_shuffles = int(input())
lst_cards_in = str_in.split()
lst_card_out = []
L_deck = lst_cards_in[0:len(lst_cards_in)//2]
R_deck = lst_cards_in[len(lst_cards_in)//2::]
tmp = ''
for n in range(n_shuffles):
    for i in range(0, len(L_deck)):
        lst_card_out.append(L_deck[i])
        lst_card_out.append(R_deck[i])
    lst_cards_in[:] = lst_card_out[:]
    lst_card_out = []
    L_deck = lst_cards_in[0:len(lst_cards_in) // 2]
    R_deck = lst_cards_in[len(lst_cards_in) // 2::]
print(lst_cards_in)

