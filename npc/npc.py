from traits.gender import generate_gender
from traits.race import generate_race 
from traits.hair_colour import generate_hair_colour


class NPC:
    def __init__(self):
        self.gender = generate_gender()
        self.race = generate_race()
        self.hair_colour = generate_hair_colour()

        
    def __str__(self):
        return f"{self.gender} {self.race} with {self.hair_colour} hair"
    
    