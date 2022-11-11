"""
Write a program that translates messages from Morse code to English
(capital letters). Use this page to help you (without the numbers).
The words will be separated by a space (' '). Each word is separated by a ' | '.
Print the found words on one line, separated by a space.
"""

morse_alphabet = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                  '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                  '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                  '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                  '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                  '..-': 'U', '...-': 'V', '.--': 'W', '-.--': 'Y', '--..': 'Z'}

in_message = input().split(' | ')
out_message = ''
for word in in_message:
    word = word.split(' ')
    for letter in word:
        for k in morse_alphabet:
            if k == letter:
                out_message += morse_alphabet[k]
    out_message += ' '

print(out_message)
