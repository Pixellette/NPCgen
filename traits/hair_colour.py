import random

WEIGHTED_HAIR_COLOURS_BY_RACE = {
    "Human": [("Brown", 30), ("Black", 30), ("Blonde", 20), ("Red", 10), ("Gray", 15)],
    "Elf": [("Green", 40), ("Pink", 30), ("Blue", 20), ("Orange", 5), ("Purple", 5)],
    "Dwarf": [("Brown", 35), ("Black", 30), ("Red", 20), ("Gray", 10), ("Blonde", 5)],
    "Orc": [("Black", 40), ("Brown", 30), ("Red", 20), ("Gray", 5), ("Blonde", 5)]
    # Add more
}


def generate_hair_colour(race):
    options = WEIGHTED_HAIR_COLOURS_BY_RACE.get(race, [("unknown", 1)])
    colours, weights = zip(*options)
    return random.choices(colours, weights=weights, k=1)[0]

#def generate_hair_colour():
#    hairColour = ["Brown", "Black", "Blonde", "Red", "Gray"]
#    weights = [40, 40, 20, 10, 15]  # Higher number = more likely
#    return random.choices(hairColour, weights=weights, k=1)[0]
