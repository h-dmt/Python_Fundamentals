# "Guess A Number". "Guess A Number" is a game in which your opponent,
# "the computer", chooses a random number between "1 and 100", and your task
# is to guess this number. After each number you enter, the computer will give you
# a hint of whether the number is greater or less than the number you selected
# until you guess the correct number.

import random
print('Guess A Number \n'
      'Enter a number between 1 and 100 ...')
user_guess = str(input())
pc_guess = random.randint(1, 100)
while not user_guess.isdigit():
    print('Invalid Input. Try again... ')
    user_guess = input()
user_guess_num = int(user_guess)
while user_guess_num != pc_guess:
    if user_guess_num > pc_guess:
        print('Too High!')
        print('Try again ...')
        user_guess = str(input())
        while not user_guess.isdigit():
            print('Invalid Input. Try again... ')
            user_guess = input()
        user_guess_num = int(user_guess)
    elif user_guess_num < pc_guess:
        print('Too Low!')
        print('Try again ...')
        user_guess = str(input())
        while not user_guess.isdigit():
            print('Invalid Input. Try again... ')
            user_guess = input()
        user_guess_num = int(user_guess)
if user_guess_num == pc_guess:
    print('You guess it!')
