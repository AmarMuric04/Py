import random

print(
    """
██╗  ██╗██╗ ██████╗ ██╗  ██╗███████╗██████╗      ██████╗ ██████╗     ██╗      ██████╗ ██╗    ██╗███████╗██████╗ 
██║  ██║██║██╔════╝ ██║  ██║██╔════╝██╔══██╗    ██╔═══██╗██╔══██╗    ██║     ██╔═══██╗██║    ██║██╔════╝██╔══██╗
███████║██║██║  ███╗███████║█████╗  ██████╔╝    ██║   ██║██████╔╝    ██║     ██║   ██║██║ █╗ ██║█████╗  ██████╔╝
██╔══██║██║██║   ██║██╔══██║██╔══╝  ██╔══██╗    ██║   ██║██╔══██╗    ██║     ██║   ██║██║███╗██║██╔══╝  ██╔══██╗
██║  ██║██║╚██████╔╝██║  ██║███████╗██║  ██║    ╚██████╔╝██║  ██║    ███████╗╚██████╔╝╚███╔███╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                
                                                                 
"""
)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

NUMBER_TO_GUESS = random.randint(0, 100)
EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5


def get_guesses(difficulty):
    if difficulty == "easy":
        return EASY_DIFFICULTY
    if difficulty == "hard":
        return HARD_DIFFICULTY


def check_answer(users_guess):
    global NUMBER_TO_GUESS
    if users_guess > NUMBER_TO_GUESS:
        print("Too high.")
        return False
    elif users_guess < NUMBER_TO_GUESS:
        print("Too low")
        return False
    else:
        print("Baaaang! You got it!")
        return True


num_of_guesses = get_guesses(difficulty)
guessed = False

while not guessed and num_of_guesses != 0:
    print(f"You have {num_of_guesses} guesses left.")
    users_guess = int(input("Enter your guess: "))

    guessed = check_answer(users_guess)

    num_of_guesses -= 1
