import random 

def generate_hair_style():
    hair_styles = ["straight", "sofltly wavy", "wavey", "curly", "afro", "tight curls", "loose curls", "dreadlocks", "braided", "in braids", "undercut"]
    weights = [30, 25, 20, 15, 10]  # Higher number = more likely
    return random.choices(hair_styles, weights=weights, k=1)[0]