# Write a program to check if a number is prime.
# A prime number is a natural number greater than 1,
# not a product of two smaller natural numbers.
# The output should be True if the number is prime and False otherwise.

num_in = int(input())
is_prime = True
for i in range(2, num_in - 1):
    if num_in % i == 0:
        is_prime = False
print(is_prime)
