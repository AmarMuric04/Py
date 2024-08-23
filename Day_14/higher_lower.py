import random

from data import data


def check_answer(guess, a, b):

    if (guess == "A" and a["follower_count"] > b["follower_count"]) or (
        guess == "B" and b["follower_count"] > a["follower_count"]
    ):
        return True
    return False


def game():
    score = 0
    compare_a = random.choice(data)
    while True:
        compare_b = random.choice(data)
        while compare_b == compare_a:
            compare_b = random.choice(data)

        print(
            f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}"
        )

        print(
            """
__    __
| |  / /____
| | / / ___/
| |/ (__  )\\
|___/____(_)\n"""
        )

        print(
            f"Compare B: {compare_b['name']}, {compare_b['description']}, from {compare_b['country']}"
        )
        print(f"\nCurrent socre: {score}")
        users_guess = input("Who has more followers? Type 'A' or 'B': ")

        if check_answer(users_guess, compare_a, compare_b):
            score += 1
            print(f"That's right!")
        else:
            print("Wrong!\n")
            break
        compare_a = compare_b
        print("\n" * 20)


play = True
while play:
    print(
        """\n
╦ ╦┬┌─┐┬ ┬┌─┐┬─┐  ┌─┐┬─┐  ┬  ┌─┐┬ ┬┌─┐┬─┐
╠═╣││ ┬├─┤├┤ ├┬┘  │ │├┬┘  │  │ ││││├┤ ├┬┘
╩ ╩┴└─┘┴ ┴└─┘┴└─  └─┘┴└─  ┴─┘└─┘└┴┘└─┘┴└─\n"""
    )
    print("Welcome to the game!")
    print("Rules are simple, guess who you think has more followers!\n")
    game()
    play = input("Do you want to play again?: (y/n): ") == "y"
