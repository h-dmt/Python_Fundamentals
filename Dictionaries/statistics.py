"""
You will be receiving key-value pairs on separate lines separated by ": "
until you receive the command "statistics".
Sometimes you may receive a product more than once.
In that case, you have to add the new quantity to the existing one.
When you receive the "statistics" command, print the following:
"Products in stock:
- {product1}: {quantity1}
- {product2}: {quantity2}
…
- {productN}: {quantityN}
Total Products: {count_all_products}
Total Quantity: {sum_all_quantities}"
"""

stock = {}
str_inp = input().split(': ')

while str_inp[0] != 'statistics':
    key = str_inp[0]
    value = int(str_inp[1])
    if key not in stock:
        stock[key] = value
    else:
        stock[key] += value
    str_inp = input().split(': ')
count_all_products = len(stock)
sum_all_quantities = 0
print(f"Products in stock:")
for i in stock:
    sum_all_quantities += stock[i]
    print(f"- {i}: {stock[i]}")

print(f"Total Products: {count_all_products}")
print(f"Total Quantity: {sum_all_quantities}")

