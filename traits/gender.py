# gender.py
import random

GENDER_OPTIONS = ["Male", "Female", "Nonbinary"]

def generate_gender():
    genders = GENDER_OPTIONS
    weights = [40, 40, 20]  
    return random.choices(genders, weights=weights, k=1)[0]

