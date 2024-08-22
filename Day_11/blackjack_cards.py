import random
import time

blackjack_deck = [
    1,
    1,
    1,
    1,
    2,
    2,
    2,
    2,
    3,
    3,
    3,
    3,
    4,
    4,
    4,
    4,
    5,
    5,
    5,
    5,
    6,
    6,
    6,
    6,
    7,
    7,
    7,
    7,
    8,
    8,
    8,
    8,
    9,
    9,
    9,
    9,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
    10,
]


def update_aces(hand):
    if len(hand) > 2 and 11 in hand:
        hand[hand.index(11)] = 1
    elif len(hand) == 2 and 1 in hand:
        hand[hand.index(1)] = 11


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
