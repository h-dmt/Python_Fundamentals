"""
You will be given information about each purchase on separate lines until you
receive the command "Purchase".
Valid information should be in the format:
">>{furniture_name}<<{price}!{quantity}".
The price could be a floating-point or integer number.
You should store the names of the furniture and the total price.
In the end, print the name of each bought furniture and the total cost,
formatted to the second decimal point:
"Bought furniture:
{1st name}
{2nd name}
…
{N name}
Total money spend: {total_cost}"
"""
import re

items = []
tot_price = 0
regex_pattern = r'>>([A-Za-z]+)<<([\d]+\.?[\d]*)!([\d]+)'
buy = input()
while buy != 'Purchase':
    match = re.search(regex_pattern, buy)
    if match:
        # print(match)
        item, price, qty = match.groups()
        items.append(item)
        tot_price += float(price) * int(qty)
    buy = input()

print("Bought furniture:")
for i in items:
    print(i)
print(f"Total money spend: {tot_price:.2f}")
