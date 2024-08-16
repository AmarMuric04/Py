import random

people = ["Amar", "Muric", "Murga"]

# person_to_pay_index = random.randint(0, len(people) - 1)

# print(f"Person that will pay the bill is {people[person_to_pay_index]}")

print(f"Person that will pay the bill is {random.choice(people)}")

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes"]

fruits = [
    "Strawberries",
    "NEctarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
