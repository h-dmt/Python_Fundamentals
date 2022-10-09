"""
Write a function that checks if a given password is valid.
Password validations are:
    • It should be 6 - 10 (inclusive) characters long
    • It should consist only of letters and digits
    • It should have at least 2 digits
If a password is valid, print "Password is valid".
Otherwise, for every unfulfilled rule, print a message:
    • "Password must be between 6 and 10 characters"
    • "Password must consist only of letters and digits"
    • "Password must have at least 2 digits"
"""


def chk_length(str_pass):
    if 6 <= len(str_pass) <= 10:
        return True


def chk_alfanum(str_pass):
    if str_pass.isalnum():
        return True


def chk_digits(str_pass):
    count = 0
    for i in range(len(str_pass)):
        if str_pass[i].isdigit():
            count += 1
    if count >= 2:
        return True


password_str = input()
if chk_length(password_str) \
        and chk_alfanum(password_str) \
        and chk_digits(password_str):
    print("Password is valid")

if not chk_length(password_str):
    print("Password must be between 6 and 10 characters")
if not chk_alfanum(password_str):
    print("Password must consist only of letters and digits")
if not chk_digits(password_str):
    print("Password must have at least 2 digits")
