divisor = int(input())
limit = int(input())

for n in range(limit, 0, -1):
    if n % divisor == 0:
        print(n)
        break
