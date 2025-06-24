#race.py

import random

RACE_OPTIONS = ["Human", "Elf", "Dwarf", "Orc"]

def generate_race():
    races = RACE_OPTIONS
    weights = [50, 20, 20, 10]  
    return random.choices(races, weights=weights, k=1)[0]