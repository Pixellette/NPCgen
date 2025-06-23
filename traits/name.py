import random

def generate_name():
    first_name = ["John", "Mark", "Mary", "Jane", "Alex", "Taylor", "Jordan", "Casey"]
    Last_name = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson"]
    first =  random.choice(first_name)
    last = random.choice(Last_name)
    return f"{first} {last}"