name_1 = str(input())
name_2 = str(input())
aid_str = name_2
temp = name_1

for i in range(len(name_2)):
    aid_str = name_1[0:i] + name_2[i] + name_1[i + 1:len(name_2)]
    name_1 = aid_str
    # print(name_1)
    if temp != aid_str:
        print(name_1)
    temp = aid_str
