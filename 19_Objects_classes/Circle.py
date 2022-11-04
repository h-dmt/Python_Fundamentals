class Circle:
    __pi = 3.14

    def __init__(self, d):
        self.d = d

    def calculate_circumference(self):
        return Circle.__pi * self.d

    def calculate_area(self):
        return Circle.__pi * self.d**2 / 4

    def calculate_area_of_sector(self, ang):
        return ang * Circle.__pi / 180 * self.d**2 / 4


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
