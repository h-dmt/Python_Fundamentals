# Write a program, which sums the ASCII codes of N characters and prints the sum on the console.
# On the first line, you will receive N – the number of lines.
# On the following N lines – you will receive a letter per line.
# Print the total sum in the following format: "The sum equals: {total_sum}".
# Note: n will be in the interval [1…20].

# Use of ord() function

n_elements = int(input())
list_elements = []
ascii_list = []
sum_elements = 0
for i in range(n_elements):
    list_elements += input()
for j in list_elements:
    sum_elements += ord(j)

print(f'The sum equals: {sum_elements}')
