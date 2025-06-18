import random

def generate_gender():
    genders = ["Male", "Female", "Nonbinary"]
    weights = [40, 40, 20]  # Higher number = more likely
    return random.choices(genders, weights=weights, k=1)[0]

