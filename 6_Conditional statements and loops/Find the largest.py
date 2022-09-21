"""
Print the largest number that can be formed from the digits of the given number.
"""
num = int(input())
str_num = str(num)
aid_str_num = ''

for i in range(len(str_num)-1):
    for j in range(i+1, len(str_num)):
        if str_num[j] > str_num[i]:
            aid_str_num = str_num[0:i] + str_num[j] + str_num[i+1:j] + str_num[i] + str_num[j+1:]
            str_num = aid_str_num
            aid_str_num = ''

print(int(str_num))


