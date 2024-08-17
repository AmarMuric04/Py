import random

word_list = ["amar", "murga", "muric"]

chosen_word = random.choice(word_list)
num_of_lives = 6
print(chosen_word)
placeholder = ""


while num_of_lives != 0 or placeholder != chosen_word:
    users_guess = input("Guess a letter: ").lower()
    letter_found = False

    for letter in chosen_word:
        if letter != users_guess:
            placeholder += "_"
        else:
            placeholder += letter
            letter_found = True

    if not letter_found:
        print("You lose a life.")
    else:
        print("You found a letter!")

    print(placeholder)
