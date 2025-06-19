import random

def generate_hair_length():
    hair_length = ["Short", "Medium", "Long", "Bald", "Extremely Long"]
    weights = [10, 20, 10, 5, 5]  # Higher number = more likely
    return random.choices(hair_length, weights=weights, k=1)[0]
