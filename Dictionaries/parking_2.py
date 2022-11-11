"""
The program receives 2 types of commands:
    • "register {username} {license_plate_number}":
        ◦ The system only supports one car per user at the moment,
        so if a user tries to register another license plate using the same
        username, the system should print:
        "ERROR: already registered with plate number {license_plate_number}"
        ◦ If the check above passes successfully, the user should be registered,
            so the system should print:
        "{username} registered {license_plate_number} successfully"
    • "unregister {username}":
        ◦ If the user is not present in the database, the system should print:
        "ERROR: user {username} not found"
        ◦ If the check above passes successfully, the system should print:
        "{username} unregistered successfully"
After you execute all of the commands, print all the currently registered users
and their license plates in the format:
    • "{username} => {license_plate_number}"
"""

n = int(input())
users = {}

for _ in range(n):
    command = input().split()
    username = command[1]
    if command[0] == 'register':
        plate_num = command[2]
        if username in users:
            print(f"ERROR: already registered with plate number {users[username]}")
        else:
            users[username] = plate_num
            print(f"{username} registered {plate_num} successfully")

    elif command[0] == 'unregister':
        if username not in users:
            print(f"ERROR: user {username} not found")
        else:
            del users[username]
            print(f"{username} unregistered successfully")

for users, plate_n in users.items():
    print(f"{users} => {plate_n}")
