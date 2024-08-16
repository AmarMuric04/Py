import random

print("Rock... Paper... SCISSOOOORRRSSS!!!!")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_move = int(input("What's your move? 0 for Rock, 1 for Paper and 2 for Scissors: "))
computer_move = random.randint(0, 2)

if user_move == 0:
    print(rock)
    print("Computer chose:")
    if computer_move == 0:
        print(rock)
        print("Draw!")
    elif computer_move == 1:
        print(paper)
        print("You lose!")
    else:
        print(scissors)
        print("You win!")
elif user_move == 1:
    print(paper)
    print("Computer chose:")
    if computer_move == 0:
        print(rock)
        print("You win!")
    elif computer_move == 1:
        print(paper)
        print("Draw!")
    else:
        print(scissors)
        print("You lose!")
elif user_move == 2:
    print(scissors)
    print("Computer chose:")
    if computer_move == 0:
        print(rock)
        print("You lose!")
    elif computer_move == 1:
        print(paper)
        print("You win!")
    else:
        print(scissors)
        print("Draw!")
