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