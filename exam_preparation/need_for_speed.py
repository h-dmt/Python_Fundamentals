"""
you will receive an integer n – the number of cars that you can obtain.
On the next n lines, the cars themselves will follow with their mileage and
fuel available, separated by "|" in the following format:
"{car}|{mileage}|{fuel}"
Then, you will be receiving different commands, each on a new line, separated by
" : ", until the "Stop" command is given:

     • "Drive : {car} : {distance} : {fuel}":
        ◦ You need to drive the given distance, and you will need the given fuel
        to do that. If the car doesn't have enough fuel, print:
        "Not enough fuel to make that ride"
        ◦ If the car has the required fuel available in the tank, increase its
        mileage with the given distance, decrease its fuel with the given fuel,
        and print:
"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
        ◦ You like driving new cars only, so if a car's mileage reaches
        100 000 km, remove it from the collection(s) and print:
        "Time to sell the {car}!"
    • "Refuel : {car} : {fuel}":
        ◦ Refill the tank of your car.
        ◦ Each tank can hold a maximum of 75 liters of fuel, so if the given
        amount of fuel is more than you can fit in the tank, take only what is
        required to fill it up.
        ◦ Print a message in the following format:
        "{car} refueled with {fuel} liters"
    • "Revert : {car} : {kilometers}":
        ◦ Decrease the mileage of the given car with the given kilometers and
        print the kilometers you have decreased it with in the following format:
"{car} mileage decreased by {amount reverted} kilometers"
        ◦ If the mileage becomes less than 10 000km after it is decreased,
        just set it to 10 000km and DO NOT print anything.

Upon receiving the "Stop" command, you need to print all cars in your possession
in the following format:
"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
"""


class Garage:

    def __init__(self):
        self.collection = {}

    def add_car(self, car, dist: int, fuel: int):
        self.collection[car] = [dist, fuel]

    def drive(self, select_car: str, drive_distance: int, drive_gas: int):
        # check enough fuel
        if drive_gas <= self.collection[car][1]:
            # decrease consumed fuel, add km and print new value
            self.collection[car][0] += drive_distance
            self.collection[car][1] -= drive_gas
            print(f"{select_car} driven for {drive_distance} kilometers. "
                  f"{drive_gas} liters of fuel consumed.")
        # if mileage > 100 000km remove car from garage
            if self.collection[select_car][0] >= 100000:
                self.collection.pop(select_car)
                print(f"Time to sell the {select_car}!")
        else:
            print("Not enough fuel to make that ride")

    def refuel(self, car: str, fuel: int):
        # check max thank capacity : 75l
        old_fuel = self.collection[car][1]
        self.collection[car][1] += fuel
        if self.collection[car][1] > 75:
            amount = 75 - old_fuel
            self.collection[car][1] = 75
            fuel = amount
        # print refuel info
        print(f"{car} refueled with {fuel} liters")

    def revert(self, car: str, km: int):
        # decrease mileage and print new value
        self.collection[car][0] -= km
        if self.collection[car][0] >= 10000:
            print(f"{car} mileage decreased by {km} kilometers")
        else:
            self.collection[car][0] = 10000
        # if mileage < 10 000 do not print anything

    def show_cars(self):
        for auto in self.collection:
            print(f"{auto} -> Mileage: {self.collection[auto][0]} kms, "
                  f"Fuel in the tank: {self.collection[auto][1]} lt.")


n = int(input())
my_garage = Garage()
# Add the cars to the garage
for i in range(n):
    car, distance, fuel = input().split('|')
    my_garage.add_car(car, int(distance), int(fuel))

# Play
while True:
    usr_inp = input().split(' : ')
    if usr_inp[0] == 'Stop':
        break
    elif usr_inp[0] == 'Drive':
        car, distance, fuel = usr_inp[1:]
        if car in my_garage.collection:
            my_garage.drive(car, int(distance), int(fuel))
    elif usr_inp[0] == 'Refuel':
        car, fuel = usr_inp[1:]
        if car in my_garage.collection:
            my_garage.refuel(car, int(fuel))
    elif usr_inp[0] == 'Revert':
        car, km = usr_inp[1:]
        if car in my_garage.collection:
            my_garage.revert(car, int(km))
    # print(my_garage.collection[car])

my_garage.show_cars()
