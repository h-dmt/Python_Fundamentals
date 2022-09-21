N = int(input())
capsule = 0.01
days = 1
price = 0
total = 0
n_cap_day = 1
for _ in range(N):
    capsule = float(input())
    days = int(input())
    n_cap_day = int(input())
    if capsule < 0.01 or capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif n_cap_day < 1 or n_cap_day > 2000:
        continue
    price = n_cap_day * days * capsule
    print(f'The price for the coffee is: ${price:.2f}')
    total += price
print(f'Total: ${total:.2f}')
