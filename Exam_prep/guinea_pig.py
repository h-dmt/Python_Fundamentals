"""
On the first three lines, you will receive the quantity of food, hay, and cover,
which Merry buys for a month (30 days). On the fourth line, you will receive the
guinea pig's weight.
Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet,
then gives it a certain amount of hay equal to 5% of the rest of the food.
On every third day, Merry puts Puppy cover with a quantity of 1/3 of its weight.
Calculate whether the quantity of food, hay, and cover, will be enough for a
month.
If Merry runs out of food, hay, or cover, stop the program!
Input
    • On the first line – quantity food in kilograms - a floating-point number in the range [0.0 – 10000.0]
    • On the second line – quantity hay in kilograms - a floating-point number in the range [0.0 – 10000.0]
    • On the third line – quantity cover in kilograms - a floating-point number in the range [0.0 – 10000.0]
    • On the fourth line – guinea's weight in kilograms - a floating-point number in the range [0.0 – 10000.0]
Output
    • If the food, the hay, and the cover are enough, print:
        ◦ "Everything is fine! Puppy is happy! Food: {excessFood}, Hay: {excessHay}, Cover: {excessCover}."
    • If one of the things is not enough, print:
        ◦ "Merry must go to the pet store!"
"""

food_qty = float(input())
hay_qty = float(input())
cover_qty = float(input())
pig_w = float(input())
second_day = 0
third_day = 0
enough_stuff = True
for days in range(1, 31):
    food_qty -= 0.3
    second_day += 1
    third_day += 1
    if second_day == 2:
        hay_qty -= 0.05 * food_qty
        second_day = 0
    if third_day == 3:
        cover_qty -= pig_w/3
        third_day = 0
    if food_qty < 0.3 or hay_qty <= 0 or cover_qty <= 0:
        print("Merry must go to the pet store!")
        enough_stuff = False
        break
if enough_stuff:
    print(f"Everything is fine! Puppy is happy! Food: "
          f"{food_qty:.2f}, Hay: {hay_qty:.2f}, Cover: {cover_qty:.2f}.")
