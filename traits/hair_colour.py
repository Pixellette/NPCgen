import random

# ← Your original per‐race weighted lists stay exactly as they were
WEIGHTED_HAIR_COLOURS_BY_RACE = {
    "Human": [("Brown", 30), ("Black", 30), ("Blonde", 20), ("Red",   10), ("Gray",  15)],
    "Elf":   [("Green", 40), ("Pink",  30), ("Blue",   20), ("Orange", 5), ("Purple", 5)],
    "Dwarf": [("Brown", 35), ("Black", 30), ("Red",    20), ("Gray",  10), ("Blonde", 5)],
    "Orc":   [("Black", 40), ("Brown", 30), ("Red",    20), ("Gray",   5), ("Blonde", 5)],
    # …any other races you’ve defined…
}

# ← A generic fallback list of real‐looking hair colours
GENERIC_FALLBACK = [
    ("Black", 1), ("Brown", 1), ("Blonde", 1),
    ("Red",   1), ("Gray",  1), ("White", 1),
]

def generate_hair_colour(race):
    """
    Pick a hair colour based on race:
        1) If we have a weighted list for that race, use it.
        2) Otherwise fall back to GENERIC_FALLBACK.
    """
    # .get(race, GENERIC_FALLBACK) returns your original list
    # when race is found, or GENERIC_FALLBACK if not.
    options = WEIGHTED_HAIR_COLOURS_BY_RACE.get(race, GENERIC_FALLBACK)

    # unzip into two parallel lists
    colours, weights = zip(*options)

    # do the weighted random choice
    return random.choices(colours, weights=weights, k=1)[0]


