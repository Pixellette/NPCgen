import random

def generate_hair_colour():
    hairColour = ["Brown", "Black", "Blonde", "Red", "Gray"]
    weights = [40, 40, 20, 10, 15]  # Higher number = more likely
    return random.choices(hairColour, weights=weights, k=1)[0]
