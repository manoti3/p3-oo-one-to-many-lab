class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    def __init__(self, name="", species="", owner=None):
        self.name = name
        self.species = species
        self.owner = owner

        if species not in self.PET_TYPES:
            raise ValueError("Invalid pet type: {}".format(species))

    def feed(self):
        if self.species == 'dog':
            return "Woof! Thanks for the food!"
        elif self.species == 'cat':
            return "Meow! Yummy!"
        elif self.species == 'bird':
            return "Tweet tweet! Delicious!"
        else:
            return "Nom nom! Thanks!"

class Owner:
    pass