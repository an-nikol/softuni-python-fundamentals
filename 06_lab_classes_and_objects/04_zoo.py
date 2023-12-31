class Zoo:
    # not meant to be used outside the class
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == 'bird':
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo_object = Zoo(zoo_name)
number_of_animals = int(input())

for animal in range(number_of_animals):
    current_animal = input().split()
    animal_type = current_animal[0]
    animal_name = current_animal[1]
    zoo_object.add_animal(animal_type, animal_name)

info = input()
print(zoo_object.get_info(info))
