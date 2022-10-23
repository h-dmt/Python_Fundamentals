

def years_km(cars):
    cars = cars.split()
    car_type = cars[0]
    years = int(cars[1])
    km = int(cars[2])
    return car_type, years, km


def tax_calculator(type_v, yrs, km):
    taxation = 0
    if type_v == "family":
        taxation = 50
        taxation -= 5 * yrs
        taxation += 12 * (km//3000)
    elif type_v == "heavyDuty":
        taxation = 80
        taxation -= 8 * yrs
        taxation += 14 * (km // 9000)
    elif type_v == "sports":
        taxation = 100
        taxation -= 9 * yrs
        taxation += 18 * (km // 2000)
    return taxation


vehicles_lst = input().split('>>')
tot_income = 0

for vehicle in vehicles_lst:
    car, yrs_tax, km_travelled = years_km(vehicle)
    valid_types = ["family", "heavyDuty", "sports"]

    if car not in valid_types:
        print("Invalid car type.")
        continue
    else:
        tax_car = tax_calculator(car, yrs_tax, km_travelled)
        tot_income += tax_car
        print(f"A {car} car will pay {tax_car:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {tot_income:.2f} euros in taxes.")
