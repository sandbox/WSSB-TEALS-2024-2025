class Pet:
    """Defines pets and their attributes"""
    def __init__(self, animal, color, food, noise, name):
        self.animal = animal
        self.color = color
        self.food = food
        self.noise = noise
        self.name = name

pet_1 = Pet('dog', 'brown', 'cheese', 'bark', 'Lassie')
pet_2 = Pet('cat', 'black', 'pizza', 'meow', 'Kitty')
pet_3 = Pet('mouse', 'white', 'seeds', 'squeak', 'Mike')

pets = [pet_1, pet_2, pet_3]

def pet_name_and_food(list_of_pets):
    for pet in list_of_pets:
        print(pet.name)
        print(pet.food)

pet_name_and_food(pets)
