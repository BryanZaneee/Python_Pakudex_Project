class Pakuri:
    # Constructor: Initializes the pakuri object with species attribute and
    # calculates initial values for attack, defense, and speed attributes
    def __init__(self, species):
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    # Getter method: Returns the species of this critter
    def get_species(self):
        return self.species

    # Getter method: Returns the attack value for this critter
    def get_attack(self):
        return self.attack

    # Getter method: Returns the defense value for this critter
    def get_defense(self):
        return self.defense

    # Getter method: Returns the speed of this critter
    def get_speed(self):
        return self.speed

    # Setter method: Changes the attack value for this critter to new_attack
    def set_attack(self, new_attack):
        self.attack = new_attack

    # Evolve method: Modifies the critter's attributes as follows:
    # a) double the attack (multiply by 2);
    # b) quadruple the defense (multiply by 4);
    # c) triple the speed (multiply by 3)

    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3
