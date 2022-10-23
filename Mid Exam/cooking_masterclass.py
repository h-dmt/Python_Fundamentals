"""
Needed per student:
1x Pack flour, 10x eggs,1x apron

Order:
20% more aprons, every 5 pack flour 1 free
"""
import math

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

needed_flour = students
needed_eggs = students * 10
needed_aprons = math.ceil(students * 1.2)
flour_tot_price = 0
fifth = 0
difference = 0
for i in range(students):
    fifth += 1
    if fifth != 5:
        flour_tot_price += flour_price
    else:
        fifth = 0
tot_price = flour_tot_price + needed_eggs * egg_price \
            + needed_aprons * apron_price

if tot_price <= budget:
    print(f"Items purchased for {tot_price:.2f}$.")
else:
    difference = tot_price - budget
    print(f"{difference:.2f}$ more needed.")
