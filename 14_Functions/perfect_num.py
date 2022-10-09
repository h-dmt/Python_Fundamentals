"""
A perfect number is a positive integer that is equal to the sum of its proper
positive divisors. That is the sum of its positive divisors, excluding the number
itself (also known as its aliquot sum).
Write a function that receives an integer number and returns one of the following
messages:
    • "We have a perfect number!" - if the number is perfect.
    • "It's not so perfect." - if the number is NOT perfect.
Print the result on the console.
"""


def divisors_sum(num):
    sum_num = 0
    for i in range(1, num):
        if num % i == 0:
            sum_num += i
    return sum_num


number = int(input())
n_sum = divisors_sum(number)
if n_sum == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
