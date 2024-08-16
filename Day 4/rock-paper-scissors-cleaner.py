import random

print("Rock... Paper... SCISSOOOORRRSSS!!!!")


moves = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
]

user_move = int(input("What's your move? 0 for Rock, 1 for Paper and 2 for Scissors: "))
computer_move = random.randint(0, 2)

print(moves[user_move])
print("Computer chose:")
print(moves[computer_move])

if user_move == computer_move:
    print("Draw!")
elif (
    user_move == 0
    and computer_move == 2
    or user_move == 1
    and computer_move == 0
    or user_move == 2
    and computer_move == 1
):
    print("You win!")
else:
    print("You lose!")
