"""
You will receive some lines of input in the format "{contest}:{password for contest}"
until you receive "end of contests". Save that data because you will need it later.
After that you will receive other type of inputs in format
"{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions".
Here is what you need to do.
    • Check if the contest is valid (It is considered valid if you received it in the first type of input)
    • Check if the password is correct for the given contest
    • If the contest and the password is valid, save the user with the contest they
    take part in (a user can take part in many contests) and the points the user has
    in the given contest. If you receive the same contest and the same user update the
    points only if the new ones are more than the older ones.

     • On the first line, print the best user in format "Best candidate is {user} with total {total points} points.".
     • Then print all students ordered as mentioned above in format:
    "{user_name1}
    #  {contest1} -> {points}
"""


def sort_points(dct):
    names = [k for k in dct]
    sort_dct = {}
    for n in dct:
        # sort the sub-dictionary by value
        sort_dct[n] = dict(sorted(dct[n].items(), key=lambda item: item[1], reverse=True))
    #print(sort_dct)
    return sort_dct


inp_cont = input().split(':')
contests = {}
# - taking the first input -
while inp_cont[0] != 'end of contests':
    contest = inp_cont[0]
    password = inp_cont[1]
    contests[contest] = password
    inp_cont = input().split(':')

inp_usr = input().split('=>')
candidates = {}

# - taking the second input -
while inp_usr[0] != 'end of submissions':
    usr_contest = inp_usr[0]
    usr_contest_pass = inp_usr[1]
    username = inp_usr[2]
    points = inp_usr[3]

    # Valid contest?
    if usr_contest in contests:
        # Password correct?
        if usr_contest_pass == contests[usr_contest]:
            # User already has a submission?
            if username in candidates:
                # contest already submitted once?
                if usr_contest in candidates[username]:
                    # Check if the new score is higher ...
                    if points > candidates[username][usr_contest]:
                        candidates[username][usr_contest] = points
                # if new contest submission from same user:
                else:
                    candidates[username][usr_contest] = points
            # If user is new add it to dictionary
            else:
                candidates[username] = {usr_contest: points}
    inp_usr = input().split('=>')
#print(candidates)

# - find best candidate -
scores_per_candidate = {}
sum_score = 0
for candidate in candidates:
    for exam in candidates[candidate]:
        sum_score += int(candidates[candidate][exam])
    scores_per_candidate[candidate] = sum_score
    sum_score = 0
# print(scores_per_candidate)
best = ['', 0]  # [ name_best_candidate, score ]
for name in scores_per_candidate:
    if scores_per_candidate[name] > best[1]:
        best[0] = name
        best[1] = scores_per_candidate[name]
#print(best)

# - sorting -
sorted_candidates = sort_points(candidates)

# - Formatting the output -
print(f"Best candidate is {best[0]} with total {best[1]} points.")
print('Ranking:')
sorted_names = sorted(candidates)
for key_name in sorted_names:
    print(f"{key_name}")
    for subject in sorted_candidates[key_name]:
        print(f"#  {subject} -> {sorted_candidates[key_name][subject]}")
