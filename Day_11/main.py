import time

from blackjack_cards import add_card, print_cards, update_aces


def blackjack():
    players_hand = []
    dealers_hand = []

    add_card("User", players_hand)
    add_card("User", players_hand)

    add_card("Dealer", dealers_hand)
    add_card("Dealer", dealers_hand)

    update_aces(players_hand)
    update_aces(dealers_hand)

    print("\n")

    print_cards("User", players_hand)
    print_cards("Dealer", dealers_hand)

    game_over = False
    while not game_over:
        move = input("\nDo you want to hit ('hit') or stand ('stand')?: ")
        if move == "hit":
            time.sleep(0.5)
            print("You hit!\n")
            add_card("User", players_hand)
            print_cards("User", players_hand)
            if sum(players_hand) > 21:
                print("\nBusted!")
                game_over = True
            if sum(players_hand) == 21:
                move = "stand"
                print("\nYou hit a blackjack!")
                time.sleep(0.5)
        if move == "stand":
            print(f"The hidden card was a {dealers_hand[1]}")
            if sum(dealers_hand) < 17:
                time.sleep(0.5)
                print("\nLet's see what the dealer gets!")
                while not game_over:
                    time.sleep(1)
                    print("\nDealer hits!\n")
                    time.sleep(1)
                    add_card("Dealer", dealers_hand)
                    print_cards("Dealer", dealers_hand)
                    if sum(dealers_hand) == 21:
                        print("\nDealer hit a blackjack!")
                        game_over = True
                    if sum(dealers_hand) > 21:
                        print("\nDealer busts!")
                        game_over = True
                    if sum(dealers_hand) >= 17:
                        game_over = True
            else:
                game_over = True

    players_score = sum(players_hand)
    dealers_score = sum(dealers_hand)

    print("")
    if players_score > 21:
        print(f"Dealer wins with {dealers_score}")
    elif dealers_score > 21:
        print(f"You win with {players_score}")
    elif dealers_score > players_score:
        print(f"Dealer wins with {dealers_score}")
    elif players_score > dealers_score:
        print(f"You win with {players_score}")
    elif dealers_score == players_score:
        print("It's a draw!")


play = True
print(
    """
.------..------..------..------..------..------..------..------..------.
|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
| :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
| ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'`------'`------'`------'`------'"""
)
print("Welcome to blackjack!")
start = input("Are you ready? (y/n): ") == "y"

if start:
    while play:
        blackjack()
        play = input("Want to play another match? (y/n): ") == "y"
