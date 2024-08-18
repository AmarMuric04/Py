import random

from hangman_stages import stages
from hangman_words import hangman_words, win_message

print(
    """
\n\nWelcome tooooooo...\n\n$$\   $$\                                                                 
$$ |  $$ |                                                                
$$ |  $$ | $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\  
$$$$$$$$ | \____$$\ $$  __$$\ $$  __$$\ $$  _$$  _$$\  \____$$\ $$  __$$\ 
$$  __$$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |  $$ |
$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |
$$ |  $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$ |$$ |  $$ |
\__|  \__| \_______|\__|  \__| \____$$ |\__| \__| \__| \_______|\__|  \__|
                              $$\   $$ |                                  
                              \$$$$$$  |                                  
                               \______/                                   """
)

hidden_word = random.choice(hangman_words)

num_of_lives = 6

letters_used = []

placeholder_list = []
placeholder = ""
for letter in hidden_word:
    placeholder_list.append("_")
    placeholder += "_"

print(f"{placeholder} ({len(hidden_word)})")

while True:
    users_guess = input("Guess a letter: ").lower()
    letter_found = False

    if len(users_guess) > 1:
        if users_guess == hidden_word:
            print(win_message)
            print(f"\nThe hidden word was {hidden_word}!\n")
            break
        else:
            print("Oops! Not the right word!")
            print("You lose a life!")
            num_of_lives -= 1

    if users_guess in letters_used:
        print("Letter was already used. Try again!")
        continue

    letters_used.append(users_guess)

    index = 0
    for letter in hidden_word:
        if users_guess == letter:
            placeholder_list[index] = letter
            letter_found = True
        index += 1

    if not letter_found:
        print("You lose a life.")
        print(stages[num_of_lives])
        num_of_lives -= 1
    else:
        print("You found a letter!")

    placeholder = "".join(placeholder_list)
    if placeholder == hidden_word:
        print(win_message)
        print(f"Letters used: {len(letters_used)}")
        print(f"Hidden word length: {len(hidden_word)}")
        print(f"Accuracy: {(len(hidden_word) / len(letters_used) * 100):.2f}%")
        break

    if num_of_lives == -1:
        break

    print(placeholder)
    print(f"Letters used: {letters_used}\n")


if num_of_lives == -1:
    print("You lost... too bad!")
    print(f"The word was {hidden_word}!")
