#  https://judge.softuni.org/Contests/Practice/Index/2525#0
#  24-11-22

secret_mex = input()
instructions = input().split('|')
while instructions[0] != 'Decode':
    if instructions[0] == 'Move':
        # Moves the first n letters to the back of the string
        n_letters = int(instructions[1])
        group_letters = secret_mex[:n_letters]
        secret_mex = secret_mex.replace(group_letters, '')
        secret_mex += group_letters

    elif instructions[0] == 'Insert':
        # Inserts the given value before the given index in the string
        index = int(instructions[1])
        value = instructions[2]
        secret_mex = secret_mex[:index] + value + secret_mex[index:]

    elif instructions[0] == 'ChangeAll':
        # Changes all occurrences of the given substring
        # with the replacement text
        substring = instructions[1]
        replacement = instructions[2]
        secret_mex = secret_mex.replace(substring, replacement)
    instructions = input().split('|')

print(f"The decrypted message is: {secret_mex}")
