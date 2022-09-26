# Read two integer numbers and, after that, exchange their values.
# Print the variable values before and after the exchange.
a = int(input())
b = int(input())
tmp = 0

print(f"Before:\n"
      f"a = {a}\n"
      f"b = {b}")
tmp = b
b = a
a = tmp
print(f"After:\n"
      f"a = {a}\n"
      f"b = {b}")
