#  reads the path to a file and subtracts the file name and its extension.

path = input().split("\\")
name_extension = path[-1].split('.')
name = name_extension[0]
extension = name_extension[1]
print(f"File name: {name}")
print(f"File extension: {extension}")

