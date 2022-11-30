"""
On the first line of the standard input, you will receive an integer n – the number
of pieces you will initially have. On the next n lines, the pieces themselves will
follow with their composer and key, separated by "|" in the following format:
"{piece}|{composer}|{key}".
Then, you will be receiving different commands, each on a new line, separated by "|",
until the "Stop" command is given:
    • "Add|{piece}|{composer}|{key}":
        ◦ You need to add the given piece with the information about it to the other
        pieces and print:
"{piece} by {composer} in {key} added to the collection!"
        ◦ If the piece is already in the collection, print:
"{piece} is already in the collection!"
    • "Remove|{piece}":
        ◦ If the piece is in the collection, remove it and print:
"Successfully removed {piece}!"
        ◦ Otherwise, print:
"Invalid operation! {piece} does not exist in the collection."
    • "ChangeKey|{piece}|{new key}":
        ◦ If the piece is in the collection, change its key with the given one and print:
"Changed the key of {piece} to {new key}!"
        ◦ Otherwise, print:
"Invalid operation! {piece} does not exist in the collection."
Upon receiving the "Stop" command, you need to print all pieces in your collection,
sorted by their name and by the name of their composer in alphabetical order,
in the following format:
"{Piece} -> Composer: {composer}, Key: {key}"
"""


def add_composer(collect, piece_new, composer_new, k):
    collect[piece_new] = {composer_new: k}


def remove_piece(collect, piece_old):
    collect.pop(piece_old)


def change_key(collect, piece_old, new_k):
    for comp in collect[piece_old]:
        collect[piece_old][comp] = new_k


n = int(input())
instructions = input().split('|')
collection = {}
while instructions[0] != 'Stop':

    if instructions[0] == 'Add':
        piece = instructions[1]
        composer = instructions[2]
        key = instructions[3]
        if piece not in collection:
            add_composer(collection, piece, composer, key)
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif instructions[0] == 'Remove':
        piece = instructions[1]
        if instructions[1] in collection:
            remove_piece(collection, piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif instructions[0] == 'ChangeKey':
        piece = instructions[1]
        key = instructions[2]
        if piece in collection:
            change_key(collection, piece, key)
            print(f"Changed the key of {piece} to {key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    else:
        piece = instructions[0]
        composer = instructions[1]
        key = instructions[2]
        add_composer(collection, piece, composer, key)

    instructions = input().split('|')

# collection = dict(sorted(collection.items(), key=lambda i: i[0]))
for title in collection:
    for artist in collection[title]:
        print(f"{title} -> Composer: {artist}, Key: {collection[title][artist]}")
