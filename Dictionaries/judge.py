"""
    You will receive several input lines in one of the following formats:
    "{username} -> {contest} -> {points}"
    The "contest" and "username" are strings, the given "points" will be an
    integer number. You need to keep track of every contest and points of each user:
        • If the user has already participated in the contest, update their points only if
            the new ones are more than the older ones.
        • Otherwise, just save the data - contest, username, and points.
    Also, you need to keep individual statistics for each user - his/her final total points
    for all contests.
    You should end your program when you receive the command "no more time".
    At that point, you should print each contest in order of input,
    for each contest print the participants ordered by points in descending order,
    then ordered by name in ascending order. After that, you should print individual
    statistics for every participant ordered by total points in descending order, and
    then by alphabetical order.
"""


def get_data(from_inp):
    from_inp = from_inp.split(' -> ')
    name = from_inp[0]
    cont = from_inp[1]
    pts = int(from_inp[2])
    return name, cont, pts


def username_to_contest(record_usr, cont_parts): # takes a dictionary ordered by username and contests
    record_contest = {}
    for key_contest in cont_parts:
        for usr in record_usr:
            # print(f"{record_usr[usr][key_contest]}")
            if key_contest in record_usr[usr]:
                if key_contest not in record_contest:
                    record_contest[key_contest] = {usr: record_usr[usr][key_contest]}
                else:
                    record_contest[key_contest][usr] = record_usr[usr][key_contest]
    return record_contest


record = {}
user_inp = input()
dct_contests_participants = {}
# - Getting the data -
while user_inp != 'no more time':
    user, contest, points = get_data(user_inp)
    if contest not in dct_contests_participants:  # which contest how may times
        dct_contests_participants[contest] = 1
    else:
        dct_contests_participants[contest] += 1
    if user not in record:
        record[user] = {contest: points}
    elif contest not in record[user]:
        record[user][contest] = points
    elif user in record and contest in record[user]:
        dct_contests_participants[contest] -= 1
        if record[user][contest] < points:
            record[user][contest] = points
    user_inp = input()


dict_per_contest = username_to_contest(record, dct_contests_participants)  # changing the dictionary structure keyed by
                                                                           # contest

#print(record)
#print(dict_per_contest)
# printing participants per contest by ascending score
for exam in dct_contests_participants:
    print(f"{exam}: {dct_contests_participants[exam]} participants")
    i = 1
    sorted_scores = dict(sorted(dict_per_contest[exam].items(),
                                key=lambda x: (-x[1], x[0])))
    for name in sorted_scores:
        print(f"{i}. {name} <::> {sorted_scores[name]}")
        i += 1

# - Find personal total scores -

tot_scores = {}
tot = 0
for names in record:
    for elem in record[names]:
        tot += record[names][elem]
    tot_scores[names] = tot
    tot = 0

print("Individual standings")
k = 1
tot_scores = dict(sorted(tot_scores.items(), key=lambda j: (-j[1], j[0])))
for n in tot_scores:
    print(f"{k}. {n} -> {tot_scores[n]}")
    k += 1


"""
--> Input example: 
Peter -> OOP -> 350
George -> OOP -> 250
Simo -> Advanced -> 600
George -> OOP -> 300
Prakash -> OOP -> 300
Prakash -> Advanced -> 250
Ani -> JSCore -> 400
no more time
"""