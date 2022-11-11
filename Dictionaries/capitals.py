"""
Using a dictionary comprehension, write a program that receives country names
on the first line, separated by comma and space ", ", and their corresponding
capital cities on the second line (again separated by comma and space ", ").
Print each country with their capital on a separate line in the following format:
 "{country} -> {capital}".
"""

countries = input().split(', ')
capitals = input().split(', ')
# Dictionary comprehension with zip() function
countries_dictionary = {countries: capitals for countries, capitals in
                        zip(countries, capitals)}

for i in countries_dictionary:
    print(f"{i} -> {countries_dictionary[i]}")
