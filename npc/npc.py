from traits.gender import generate_gender
from traits.race import generate_race 
from traits.hair_colour import generate_hair_colour
from traits.hair_length import generate_hair_length


class NPC:
    def __init__(self):
        self.gender = generate_gender()
        self.race = generate_race()
        self.hair_length = generate_hair_length()
        if self.hair_length == "Bald":
            self.hair_colour = None
        else:
            self.hair_colour = generate_hair_colour(self.race)

    def __str__(self):
        if self.hair_length == "Bald":
            return f"a bald {self.gender} {self.race}"
        else:
            return f"{self.gender} {self.race} with {self.hair_length} {self.hair_colour} hair"