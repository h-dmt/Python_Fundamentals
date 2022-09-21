"""
You are saying goodbye to your best friend: "See you next happy year".
Happy Year is the year with only distinct digits, for example, 2018.
Write a program that receives an integer number and finds the next happy year.
"""
year = int(input())
year_set = set()
happy_year = year
while len(year_set) != len(str(happy_year)):
    year_set = set()
    happy_year += 1
    for i in str(happy_year):
        year_set.add(i)
print(f'{happy_year}')
