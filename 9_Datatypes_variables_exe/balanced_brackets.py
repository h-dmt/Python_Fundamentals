# ----------------------------------------------------------------------------#
# On the first line, you will receive n – the number of lines,                #
# which will follow. On the following n lines, you will receive               #
# one of the following:                                                       #
#     • Opening bracket – "(",                                                #
#     • Closing bracket – ")" or                                              #
#     • Random string                                                         #
# Your task is to find out if the brackets are balanced.                      #
# That means after every opening bracket should follow a closing one.         #
# Nested parentheses are not valid, and if, for example, two consecutive      #
# opening brackets exist, the expression should be marked as unbalanced.      #
# You should print "BALANCED" if the parentheses are balanced and             #
# "UNBALANCED" otherwise.                                                     #
# ----------------------------------------------------------------------------#

n_lines = int(input())
random_input = ''
open_counter = 0
status_open = False
for k in range(n_lines):
    random_input = str(input())
    if random_input == '(':
        open_counter += 1
        status_open = True
        if open_counter > 1:
            open_counter = 10
            break
    if random_input == ')' and status_open:
        open_counter -= 1
        if open_counter == 0:
            status_open = False
    elif random_input == ')' and not status_open:
        open_counter = 10
        break
if open_counter == 0:
    print('BALANCED')
else:
    print('UNBALANCED')
