import time

from blackjack_cards import add_card, get_deck, print_cards


def hand_value(hand):
    return sum(hand.values())


def blackjack(deck):
    players_hand = {}
    dealers_hand = {}
    add_card("User", players_hand, deck)
    add_card("User", players_hand, deck)

    add_card("Dealer", dealers_hand, deck)
    add_card("Dealer", dealers_hand, deck)

    print()

    time.sleep(0.5)
    print_cards("User", players_hand)
    print_cards("Dealer", dealers_hand)

    game_over = False
    while not game_over:
        move = "stand"
        if hand_value(players_hand) == 21:
            print("You hit a blackjack!")
        else:
            move = input("\nDo you want to hit ('hit') or stand ('stand')?: ")
        if move == "hit":
            time.sleep(0.5)
            print("You hit!\n")
            add_card("User", players_hand, deck)
            time.sleep(0.5)
            print_cards("User", players_hand)
            if hand_value(players_hand) > 21:
                print("\nBusted!")
                print(f"\nThe mystery card was {list(dealers_hand)[1]}")
                game_over = True
            if hand_value(players_hand) == 21:
                move = "stand"
                print("\nYou hit a blackjack!")
                time.sleep(0.5)
        if move == "stand":
            time.sleep(0.5)
            print(f"The mystery card was {list(dealers_hand)[1]}")
            if hand_value(dealers_hand) == 21:
                print("\nDealer hit a blackjack!")
                game_over = True
            elif hand_value(dealers_hand) < 17 or (
                game_type == "h17"
                and hand_value(dealers_hand) == 17
                and any(card.startswith("A") for card in dealers_hand)
            ):
                time.sleep(0.5)
                print("\nLet's see what the dealer gets!")
                while not game_over:
                    time.sleep(1)
                    print("\nDealer hits!\n")
                    time.sleep(1)
                    add_card("Dealer", dealers_hand, deck)
                    time.sleep(0.5)
                    print_cards("Dealer", dealers_hand)
                    if hand_value(dealers_hand) == 21:
                        print("\nDealer hit a blackjack!")
                        game_over = True
                    if hand_value(dealers_hand) > 21:
                        print("\nDealer busts!")
                        game_over = True
                    if hand_value(dealers_hand) >= 17:
                        game_over = True
            else:
                game_over = True

    players_score = hand_value(players_hand)
    dealers_score = hand_value(dealers_hand)

    time.sleep(1)
    print("")
    if players_score > 21:
        print(f"Dealer wins with a hand value of {dealers_score}")
    elif dealers_score > 21:
        print(f"You win with a hand value of {players_score}")
    elif dealers_score > players_score:
        print(f"Dealer wins with a hand value of {dealers_score}")
    elif players_score > dealers_score:
        print(f"You win with a hand value of {players_score}")
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
print("Welcome to Blackjack!")
print("In this game, you aim to get as close to 21 as possible without going over.")
print("Aces can be worth either 1 or 11, and face cards (J, Q, K) are worth 10.\n")
start = input("Are you ready? (y/n): ") == "y"
print("\nH17 = if the dealer has an Ace and a 6, he would hit.")
print("S17 = if the dealer has an Ace and a 6, he would stand.\n")
game_type = input("Do you want to play H17 or S17? (h17/s17): ")

if start:
    while play:
        deck = get_deck()
        blackjack(deck)
        play = input("Want to play another match? (y/n): ") == "y"

# TODO add a betting system,
