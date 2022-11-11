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


class Parking:
    def __init__(self):
        self.users = {}

    def register(self, usr: str, plate: str):
        if usr in self.users:
            print(f"ERROR: already registered with plate number {self.users[usr]}")
        else:
            self.users[usr] = plate
            print(f"{usr} registered {self.users[usr]} successfully")

    def unregister(self, usr):
        if usr not in self.users:
            print(f"ERROR: user {usr} not found")
        else:
            del self.users[usr]
            print(f"{usr} unregistered successfully")


park = Parking()
n = int(input())

for _ in range(n):
    command = input().split()
    username = command[1]
    if command[0] == 'register':
        plate_num = command[2]
        park.register(username, plate_num)
    elif command[0] == 'unregister':
        park.unregister(username)

for users, plate_n in park.users.items():
    print(f"{users} => {plate_n}")
