import random

print(
    "Welcome to the adventure game! Your goal is to survive and make the right choices."
)

move = input('You wake up in a forest. Do you "explore" the area or "rest"?\n')

if move == "explore":
    print("You found a small path leading deeper into the forest.")
    move = input('Do you want to follow the "path" or "return" to where you started?\n')
    if move == "path":
        print("The path leads to a river with a broken bridge.")
        move = input('Do you want to "cross" the bridge or "search" for another way?\n')
        if move == "cross":
            print("You carefully cross the bridge, but it starts to collapse!")
            move = input('Do you want to "jump" to the other side or "hold" on?\n')
            if move == "jump":
                print("You made it across safely!")
                move = input(
                    'You see a cave nearby. Do you want to "enter" the cave or "continue" down the path?\n'
                )
                if move == "enter":
                    print("The cave is dark and cold.")
                    move = input(
                        'Do you want to "light" a torch or "explore" in the dark?\n'
                    )
                    if move == "light":
                        print(
                            "You light a torch and discover ancient drawings on the walls."
                        )
                        move = input(
                            'Do you want to "study" the drawings or "ignore" them?\n'
                        )
                        if move == "study":
                            print(
                                "The drawings reveal a hidden treasure buried nearby!"
                            )
                            move = input(
                                'Do you want to "dig" for the treasure or "leave" it?\n'
                            )
                            if move == "dig":
                                print("You found a chest filled with gold! You won!")
                            else:
                                print(
                                    "You leave the treasure behind and continue your journey."
                                )
                                # Continue the story with further decisions...
                        else:
                            print("You ignore the drawings and move on.")
                            # Continue the story with further decisions...
                    else:
                        print(
                            "You stumble in the dark and injure yourself. You have to leave the cave."
                        )
                        # Continue the story with further decisions...
                else:
                    print("You continue down the path and encounter a wild animal.")
                    move = input('Do you want to "fight" the animal or "run" away?\n')
                    if move == "fight":
                        print("You manage to scare the animal away!")
                        move = input(
                            'You find a village ahead. Do you want to "enter" the village or "avoid" it?\n'
                        )
                        if move == "enter":
                            print(
                                "The villagers welcome you and offer food and shelter."
                            )
                            move = input(
                                'Do you want to "stay" with the villagers or "continue" your journey?\n'
                            )
                            if move == "stay":
                                print("You live peacefully in the village. You won!")
                            else:
                                print(
                                    "You continue your journey, but the road is long and dangerous."
                                )
                                # Continue the story with further decisions...
                        else:
                            print(
                                "You avoid the village and get lost in the woods. Game Over."
                            )
                    else:
                        print(
                            "You run away, but the animal chases you down. Game Over."
                        )
            else:
                print("The bridge collapses and you fall into the river. Game Over.")
        else:
            print("You search for another way and find a safer crossing downstream.")
            move = input(
                'Do you want to "cross" the river here or "camp" for the night?\n'
            )
            if move == "cross":
                print("You cross the river safely.")
                # Continue the story with further decisions...
            else:
                print("You set up camp for the night.")
                move = input(
                    'In the morning, do you "continue" your journey or "explore" the area?\n'
                )
                if move == "continue":
                    print("You continue your journey and discover a hidden valley.")
                    # Continue the story with further decisions...
                else:
                    print("You explore the area and find an abandoned mine.")
                    move = input('Do you want to "enter" the mine or "leave" it?\n')
                    if move == "enter":
                        print("The mine is dark and eerie.")
                        # Continue the story with further decisions...
                    else:
                        print("You leave the mine and continue your journey.")
                        # Continue the story with further decisions...
else:
    print("You decide to rest and gather your strength.")
    move = input(
        'After resting, do you want to "explore" the area or "stay" where you are?\n'
    )
    if move == "explore":
        print("You find a small village nearby.")
        move = input('Do you want to "visit" the village or "avoid" it?\n')
        if move == "visit":
            print("The villagers are friendly and offer you food.")
            move = input(
                'Do you want to "stay" with the villagers or "leave" the village?\n'
            )
            if move == "stay":
                print("You live peacefully in the village. You won!")
            else:
                print("You leave the village and continue your journey.")
                # Continue the story with further decisions...
        else:
            print("You avoid the village and continue wandering.")
            move = input('Do you want to "follow" the road or "explore" the woods?\n')
            if move == "follow":
                print("The road leads you to a hidden temple.")
                move = input('Do you want to "enter" the temple or "keep" walking?\n')
                if move == "enter":
                    print("Inside the temple, you find ancient relics.")
                    # Continue the story with further decisions...
                else:
                    print("You keep walking and discover a peaceful meadow.")
                    # Continue the story with further decisions...
            else:
                print("The woods are dark and full of danger.")
                move = input('Do you want to "keep" going or "turn" back?\n')
                if move == "keep":
                    print("You encounter a wild animal.")
                    # Continue the story with further decisions...
                else:
                    print("You turn back and find yourself near a small lake.")
                    # Continue the story with further decisions...
    else:
        print("You stay where you are, but nothing happens. Game Over.")
