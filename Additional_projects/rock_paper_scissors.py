import random

print('Rock - Scissors - Paper Game \n'
      'to begin please choose \n'
      '[r]ock\n'
      '[s]cissors\n'
      '[p]aper')

user_input = str(input())
while user_input != 'r'\
    and user_input != 's'\
    and user_input != 'p':
    print('Invalid Input. Try again...')
    user_input = str(input())
machine_input = random.randint(1, 3)
if machine_input == 1:
    machine_input = 'r'
    print('The computer chose Rock')
elif machine_input == 2:
    machine_input = 's'
    print('The computer chose Scissors')
else:
    machine_input = 'p'
    print('The computer chose Paper')

if user_input == 'r':
    if machine_input == 'r':
        print('Draw')
    elif machine_input == 's':
        print('You win')
    elif machine_input == 'p':
        print('You lose')
elif user_input == 'p':
    if machine_input == 'r':
        print('You win')
    elif machine_input == 's':
        print('You lose')
    elif machine_input == 'p':
        print('Draw')
elif user_input == 's':
    if machine_input == 'r':
        print('You lose')
    elif machine_input == 's':
        print('Draw')
    elif machine_input == 'p':
        print('You win')
