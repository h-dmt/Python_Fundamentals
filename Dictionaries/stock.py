"""
You will be given key-value pairs of products and quantities
(on a single line separated by space). On the following line,
you will be given products to search for. Check for each product.
You have 2 possibilities:
    • If you have the product, print "We have {quantity} of {product} left".
    • Otherwise, print "Sorry, we don't have {product}".
"""


def make_dct(lst):
    dct = {}
    for i in range(0, len(lst), 2):
        key = inventory_lst[i]
        value = inventory_lst[i + 1]
        dct[key] = value
    return dct


inventory_lst = input().split(' ')
look_for_items = input().split(' ')
inventory_dct = make_dct(inventory_lst)

for item in look_for_items:
    if item in inventory_dct:
        quantity = inventory_dct[item]
        print(f"We have {quantity} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
