"""
You are given a collection of tickets separated by commas and spaces
(one or many). You need to check each ticket to see if it has
a winning combination of symbols:
    • A valid ticket has exactly 20 characters.
    • A winning ticket is a valid one, containing one of the symbols
    '@', '#', '$' or '^' uninterruptedly repeated at least 6 times in both halves
    of the tickets.
    • In order to win a Jackpot, the ticket should contain the same winning
    symbol 10 times on both sides
An example of a valid winning ticket:
"Cash$$$$$$Ca$$$$$$sh"
An example of a Jackpot winning valid ticket:
"$$$$$$$$$$$$$$$$$$$$"
"""


def check_valid(this_one):
    is_valid = False
    if len(this_one) == 20:
        is_valid = True
    return is_valid


def check_combo(this_ticket):
    win = False
    comb = []
    previous = ''
    count = 1
    win_symb = ''
    for symbol in this_ticket:
        if symbol == '@' or symbol == '#' or symbol == '$' or symbol == '^':
            if symbol == previous:
                count += 1
            else:
                count = 1
            #  check number of repetitions
            if count == 6:
                win = True
                comb = [str(count), symbol]
            elif count == 10:
                win = True
                comb = [str(count), symbol, 'Jackpot!']
                return win, comb
        previous = symbol
    return win, comb


tickets = input().split(', ')

for ticket in tickets:
    ticket = ticket.strip()
    valid = check_valid(ticket)
    if valid:
        half_1 = ticket[:10]
        half_2 = ticket[10:20]
        winning_1, combo_1 = check_combo(half_1)
        winning_2, combo_2 = check_combo(half_2)
        #print(f"{winning_1}, {combo_1}")
        #print(f"{winning_2}, {combo_2}")
        if winning_1 and winning_2:
            if len(combo_1) < 3 or\
                    len(combo_2) < 3 and\
                    combo_1[1] == combo_2[1]:  # WIN - No Jackpot
                print(f"ticket \"{ticket}\" - {combo_1[0] + combo_1[1]}")
            elif len(combo_1) == 3 and\
                    len(combo_2) == 3 and\
                    combo_1[1] == combo_2[1]:  # WIN - Jackpot
                print(f"ticket \"{ticket}\" - {combo_1[0] + combo_1[1]} Jackpot!")
        else:
            print(f"ticket \"{ticket}\" - no match")
    else:
        print("invalid ticket")
