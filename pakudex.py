from pakuri import Pakuri
class Pakudex:
    # Constructor: Initializes the object as storing 0 pakuri and
    # sets the capacity to the user-defined value or default of 20
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuri_list = []

    # Getter method: Returns the number of critters currently in the pakudex
    def get_size(self):
        return len(self.pakuri_list)

    # Getter method: Returns the maximum number of critters the pakudex can hold
    def get_capacity(self):
        return self.capacity

    # Getter method: Returns a list containing the species of the critters in the pakudex
    # or returns None if no species have been added yet
    def get_species_array(self):
        if not self.pakuri_list:
            return None
        return [pakuri.get_species() for pakuri in self.pakuri_list]

    # Getter method: Returns a list containing the attack, defense, and speed stats
    # of a given species, or None if the species is not in the pakudex
    def get_stats(self, species):
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return None

    # Sort method: Sorts the pakuri objects in the pakudex according to the
    # Python standard lexicographical ordering of species name
    def sort_pakuri(self):
        self.pakuri_list.sort(key=lambda pakuri: pakuri.get_species())

    # Add method: Adds a new species to the pakudex if it's not already present
    # and if there's enough capacity; returns True if successful, False otherwise
    def add_pakuri(self, species):
        if self.get_size() < self.capacity:
            for pakuri in self.pakuri_list:
                if pakuri.get_species() == species:
                    return False
            new_pakuri = Pakuri(species)
            self.pakuri_list.append(new_pakuri)
            return True
        return False

