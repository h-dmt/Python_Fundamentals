input_string = str(input())
output_string = ''
while input_string != 'End':
    for i in input_string:
        output_string += i + i
    if input_string != 'SoftUni':
        print(output_string)
    output_string = ''
    input_string = str(input())
