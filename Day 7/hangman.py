import random

word_list = ["amar", "murga", "muric"]

chosen_word = random.choice(word_list)
num_of_lives = 6
print(chosen_word)
placeholder_list = []

for letter in chosen_word:
    placeholder_list.append("_")

while num_of_lives != 0:
    users_guess = input("Guess a letter: ").lower()
    letter_found = False

    index = 0
    for letter in chosen_word:
        if users_guess == letter:
            placeholder_list[index] = letter
            letter_found = True
        index += 1

    if not letter_found:
        print("You lose a life.")
        num_of_lives -= 1
    else:
        print("You found a letter!")

    placeholder = "".join(placeholder_list)
    if placeholder == chosen_word:
        print("You win. Congrats!")
        break
    print(placeholder)

if num_of_lives == 0:
    print("You lost... too bad!")
