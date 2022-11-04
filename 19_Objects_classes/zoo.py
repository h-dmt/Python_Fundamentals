class Zoo:
    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        else:
            self.birds.append(name)

    def get_info(self, specie_info):
        tot_animals = len(self.mammals) + len(self.fishes) + len(self.birds)
        if specie_info == 'mammal':
            return f"Mammals in {self.name_zoo}: {', '.join(self.mammals)} \n" \
                   f"Total animals: {tot_animals}"
        elif specie_info == 'fish':
            return f"Fishes in {self.name_zoo}: {', '.join(self.fishes)} \n" \
                   f"Total animals: {tot_animals}"
        else:
            return f"Birds in {self.name_zoo}: {', '.join(self.birds)} \n" \
                   f"Total animals: {tot_animals}"


zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())
for _ in range(n):
    animal = input().split()
    in_specie = animal[0]
    in_name = animal[1]
    zoo.add_animal(in_specie, in_name)

info_specie = input()
print(zoo.get_info(info_specie))
