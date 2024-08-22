import random
import time

from blackjack_cards import blackjack_deck


def update_aces(hand):
    if len(hand) > 2 and 11 in hand:
        hand[hand.index(11)] = 1
    elif len(hand) == 2 and 1 in hand:
        hand[hand.index(1)] = 11


def add_card(player, hand):
    card = random.choice(blackjack_deck)
    blackjack_deck.remove(card)
    if card == 1 and not 11 in hand:
        card = 11
    hand.append(card)
    update_aces(hand)
    time.sleep(0.5)
    if player == "Dealer" and len(hand) == 2:
        print("Dealer gets a mystery card!")
    else:
        print(f"{player} gets a {card}!")


def print_cards(player, hand):
    print(f"{player}'s cards: ")
    if player == "Dealer" and len(hand) == 2:
        print(" ___   ___ ", end=" ")
        print()
        symbol = hand[0]
        if symbol == 11:
            symbol = "A"
        if symbol == 10:
            symbol = "K"
        print(f"|{symbol}  | |#  |", end=" ")
        print()

        print("| ⚭ | | # |", end=" ")
        print()

        print(f"|__{symbol}| |__#|", end=" ")
        print()
    else:
        for card in hand:
            print(" ___ ", end=" ")

        print()

        for card in hand:
            symbol = card
            if symbol == 11:
                symbol = "A"
            if symbol == 10:
                symbol = "K"
            print(f"|{symbol}  |", end=" ")

        print()

        for _ in hand:
            print("| ⚭ |", end=" ")

        print()

        for card in hand:
            symbol = card
            if symbol == 11:
                symbol = "A"
            if symbol == 10:
                symbol = "K"
            print(f"|__{symbol}|", end=" ")

        print(f" ({sum(hand)})")


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
    if players_score > 21 or dealers_score > players_score:
        print(f"Dealer wins with {dealers_score}")
    elif dealers_score > 21 or players_score > dealers_score:
        print(f"You win with {players_score}")
    elif dealers_score == players_score:
        print("It's a draw!")


play = True
print("Welcome to blackjack!")
start = input("Are you ready? (y/n): ") == "y"

if start:
    while play:
        blackjack()
        play = input("Want to play another match? (y/n): ") == "y"

# print(blackjack_deck)
