"""
Write a function that calculates the total price of an order and returns it.
The function should receive one of the following products: "coffee", "coke",
"water", or "snacks", and a quantity of the product.
The prices for a single piece of each product are:

    • coffee - 1.50
    • water - 1.00
    • coke - 1.40
    • snacks - 2.00

Print the result formatted to the second decimal place.

"""

product = input()
qty = int(input())
prices = {'coffee': 1.50, 'water': 1, 'coke': 1.40, 'snacks': 2}
cash = prices[product]
tot = lambda value, n: value * n
print(f"{tot(cash, qty):.2f}")
