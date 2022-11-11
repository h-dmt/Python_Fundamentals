"""
You will be receiving company names and an employees' id until you receive the
command "End" command. Add each employee to the given company.
Keep in mind that a company cannot have two employees with the same id.
Print the company name and each employee's id in the following format:
"{company_name}
-- {id1}
-- {id2}
…
-- {idN}"
Input / Constraints
    • Until you receive the "End" command, you will be receiving input in the
    format:
"{company_name} -> {employee_id}".
    • The input always will be valid.
"""

user_input = input().split(' -> ')
users_data = {}
while user_input[0] != 'End':
    name = user_input[0]
    id_n = [user_input[1]]
    if name not in users_data:
        users_data[name] = id_n
    elif id_n[0] not in users_data[name]:
        users_data[name].append(id_n[0])
    user_input = input().split(' -> ')

for names in users_data:
    print(f"{names}")
    for ids in users_data[names]:
        print(f"-- {ids}")
