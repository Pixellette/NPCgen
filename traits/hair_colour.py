# hair_colour.py

import random

# ── 1) Named colour palettes ─────────────────────────────────────────
GENERIC = [("Light Brown", 1), ("Dark Brown", 1), ("Chestnut", 1),
           ("Strawberry Blonde", 1), ("Ash Blonde", 1), ("Platinum Blonde", 1), ("Dirty Blonde", 1), ("Blonde", 1), 
           ("Red", 1), ("Ginger", 1), ("Auburn", 1), ("Copper", 1), ("Burgundy", 1),
           ("Black", 1), ("Gray", 1), ("White", 1)]

BRIGHTS = [("Pink", 1), ("Hot Pink", 1), ("Magenta", 1), ("Violet", 1), 
           ("Purple", 1), ("Lavender", 1),
           ("Blue", 1), ("Electric Blue", 1), ("Cyan", 1), ("Turquoise", 1),
           ("Green", 1), ("Orange", 1), ("Yellow", 1)]

NORDIC = [("Blonde", 1), ("Ash Blonde", 1), ("Platinum Blonde", 1), ("Dirty Blonde", 1), ("Strawberry Blonde", 1), ("Light Brown", 1),
              ("Red", 1), ("Ginger", 1), ("Copper", 1), ("Auburn", 1), ("Burgundy", 1),
              ("Gray", 1), ("White", 1)]

# “Plain” neutrals—common, uncomplicated tones
PLAIN = [
    ("Black",      1),
    ("Brown",      1),
    ("Blonde",     1),
    ("Red",        1),
    ("Chestnut",   1),
    ("Auburn",     1),
    ("Gray",       1),
    ("White",      1),
]

# “Nature” palette—earthy and plant‐inspired hues
NATURE = [
    ("Forest Green", 1),
    ("Moss Green",   1),
    ("Earth Brown",  1),
    ("Chestnut",     1),
    ("Amber",        1),
    ("Rust",         1),
    ("Sandy Blonde", 1),
    ("Gold",         1),
]

# ── 2) Fallback that merges all palettes, but leans on GENERIC ────────
# Combine every colour once, giving GENERIC colours weight*3, others weight 1
_all_palettes = GENERIC + BRIGHTS + NORDIC + PLAIN + NATURE
_fallback_weights = {}
for colour, w in _all_palettes:
    # If it's in GENERIC, triple its base weight; otherwise just 1
    base = w
    if any(colour == g[0] for g in GENERIC):
        _fallback_weights[colour] = _fallback_weights.get(colour, 0) + base * 3
    else:
        _fallback_weights[colour] = _fallback_weights.get(colour, 0) + 1

FALLBACK = list(_fallback_weights.items())


# ── 3) Map each race to a list of (palette, palette_weight) ───────
RACE_PALETTES = {
    "Human": [
        (GENERIC, 90),
        (BRIGHTS, 10),        # small chance of dye
    ],
    "Elf": [
        (GENERIC, 40),
        (BRIGHTS, 20),
        (NATURE, 20),
        (PLAIN,  20),
    ],
    "Dwarf": [
        (GENERIC, 50),
        (NORDIC,  50),        # dwarves skew Nordic but still human tones
    ],
    "Orc": [
        (GENERIC, 60),
        (BRIGHTS,  5),
        (NATURE,  20),
        (PLAIN,   15),
    ],
    # …add other races, e.g. “Gnome”: [(BRIGHTS,80),(PLAIN,20)], etc.
}

def generate_hair_colour(race, debug=False):
    """
    1) Pick one palette based on RACE_PALETTES[race] (or FALLBACK)
    2) Pick one colour from that palette
    3) If debug=True, print out trace info
    """

    # 1) Choose palette
    choices = RACE_PALETTES.get(race, [(FALLBACK, 100)])
    palettes, pweights = zip(*choices)
    chosen_palette = random.choices(palettes, weights=pweights, k=1)[0]

    
    # extract just the colour names for readability
    palette_names = [colour for colour, _ in chosen_palette]
    print(f"[DEBUG] Race '{race}' → palette picked: {palette_names}")

    # 2) Choose colour from that palette
    colours, cweights = zip(*chosen_palette)
    chosen_colour = random.choices(colours, weights=cweights, k=1)[0]


    print(f"[DEBUG] Colour selected: {chosen_colour}\n")

    return chosen_colour

