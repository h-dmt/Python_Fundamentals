"""
You will be receiving lines in the following format:
"{username}-{language}-{points}" until you receive "exam finished".
You should store each username and their submissions and points.
If a student has two or more submissions for the same language, save only his
maximum points.
You can receive a command to ban a user for cheating in the following format:
"{username}-banned". In that case, you should remove the user from the contest but
preserve his submissions in the total count of submissions for each language.
After receiving "exam finished", print each of the participants in the following
format:
"Results:
{username1} | {points}
{username2} | {points}
…
{usernameN} | {points}"
"""
