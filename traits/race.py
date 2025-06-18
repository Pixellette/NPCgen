import random

def generate_race():
    races = ["Human", "Elf", "Dwarf", "Orc"]
    weights = [50, 20, 20, 10]  # Higher number = more likely
    return random.choices(races, weights=weights, k=1)[0]