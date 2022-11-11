"""
Input
    • Until you receive "buy", the products will be coming in the format:
    "{name} {price} {quantity}".
    • The product data is always delimited by a single space.
Output
    • Print information about each product in the following format:
    "{product_name} -> {total_price}"
    • Format the total price to the 2nd digit after the decimal separator.
"""

products = input().split()
dct_buy = {}
while products[0] != 'buy':
    key = products[0]
    price = float(products[1])
    qty = int(products[2])

    if key not in dct_buy:
        dct_buy[key] = [price, qty]
    else:
        dct_buy[key][1] += qty
        if dct_buy[key][0] != price:
            dct_buy[key][0] = price

    products = input().split()

for prod in dct_buy:
    total_price = dct_buy[prod][0] * dct_buy[prod][1]
    print(f"{prod} -> {total_price:.2f}")
