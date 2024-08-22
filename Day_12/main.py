enemies = 1


def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")


increase_enemies()
print(f"Enemies outside function: {enemies}")


# Local scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)


# drink_potion()
# print(potion_strength)

# Global scope
player_health = 10


def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()


# game()
# print(player_health)

# There is no Block Scope in Python :O

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    new_enemy = " "
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)


# create_enemy()

# Editing a global variable

enemies = 1


def increase_enemies():
    global enemies
    enemies = 2
    # print(f"Enemies inside function: {enemies}")


# print(f"Enemies outside function: {enemies}")

enemies = 1


def increase_enemies(enemy):
    print(f"Enemies inside function: {enemies}")
    return enemy + 1


enemies = increase_enemies(enemies)
print(f"Enemies outside function: {enemies}")

# Constants

PI = 3.14159
GOOGLE_URL = "www.google.com"
