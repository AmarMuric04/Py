import random

import hangman_stages
import hangman_words

chosen_word = random.choice(hangman_words.hangman_words)

num_of_lives = 6

letters_used = []

placeholder_list = []
placeholder = ""
for letter in chosen_word:
    placeholder_list.append("_")
    placeholder += "_"

print(f"{placeholder} ({len(chosen_word)})")

while True:
    users_guess = input("Guess a letter: ").lower()
    letter_found = False

    if users_guess in letters_used:
        print("Letter was already used. Try again!")
        continue

    letters_used.append(users_guess)

    index = 0
    for letter in chosen_word:
        if users_guess == letter:
            placeholder_list[index] = letter
            letter_found = True
        index += 1

    if not letter_found:
        print("You lose a life.")
        print(hangman_stages.stages[num_of_lives])
        num_of_lives -= 1
    else:
        print("You found a letter!")

    placeholder = "".join(placeholder_list)
    if placeholder == chosen_word:
        print(hangman_words.win_message)
        print(f"Letters used: {len(letters_used)}")
        print(f"Hidden word length: {len(chosen_word)}")
        print(f"Accuracy: {(len(chosen_word) / len(letters_used) * 100):.2f}%")
        break

    if num_of_lives == -1:
        break

    print(placeholder)
    print(f"Letters used: {letters_used}\n")


if num_of_lives == -1:
    print("You lost... too bad!")
    print(f"The word was {chosen_word}!")
