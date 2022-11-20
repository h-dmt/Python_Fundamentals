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


def fill_data(dict_submissions, username, language, points):

    if username not in dict_submissions:  # if new user add user
        dict_submissions[username] = {language: points}
        # if not first submission
    elif username in dict_submissions and language in dict_submissions[username]:
        if points > dict_submissions[username][language]:  # save only the highest score
            dict_submissions[username][language] = points
        #  if first submission for the language
    elif username in dict_submissions and language not in dict_submissions[username]:
        dict_submissions[username][language] = points

    return dict_submissions


submission = input().split('-')
dictionary_submissions = {}
languages_submission = {}

while submission[0] != 'exam finished':
    if len(submission) == 3:
        user, lang, p = submission[:]
        if lang not in languages_submission:
            languages_submission[lang] = 1
        else:
            languages_submission[lang] += 1
        dictionary_submissions = fill_data(dictionary_submissions, user, lang, p)
    elif len(submission) == 2:
        user = submission[0]
        dictionary_submissions.pop(user)
    submission = input().split('-')
#  Print output
print('Results:')
for key in dictionary_submissions:  # for every student in dictionary
    for lecture in dictionary_submissions[key]:  # for every language per student
        score = dictionary_submissions[key][lecture]  # get the score
        print(f"{key} | {score}")
print('Submissions:')
for title in languages_submission:
    n = languages_submission[title]
    print(f"{title} - {n}")
