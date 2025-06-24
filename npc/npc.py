# npc/npc.py

# ── Imports for each trait generator ─────────────────────────────────────
from traits.name import generate_name
from traits.gender import generate_gender
from traits.race import generate_race
from traits.hair_length import generate_hair_length
from traits.hair_colour import generate_hair_colour
from traits.hair_style import generate_hair_style

class NPC:
    def __init__(self):
        # 1) Generate and store each piece of data as an attribute
        self.name        = generate_name()
        self.gender      = generate_gender()
        self.race        = generate_race()
        self.hair_length = generate_hair_length()

        # 2) If they’re bald, skip colour/style; otherwise call both generators
        if self.hair_length == "Bald":
            self.hair_colour = None
            self.hair_style  = None
        else:
            # pass race context into colour generator
            self.hair_colour = generate_hair_colour(self.race)
            self.hair_style  = generate_hair_style()

        # 3) TODO: Placeholder “longer” description for now
        self.description = "Is a neat person"

    def __str__(self):
        # Fallback single-line when someone does `str(npc)`
        if self.hair_length == "Bald":
            return f"{self.name}, a bald {self.gender} {self.race}"
        else:
            return (
                f"{self.name}, a {self.gender} {self.race} "
                f"with {self.hair_length} {self.hair_colour} hair"
            )
