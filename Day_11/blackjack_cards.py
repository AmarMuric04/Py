import random
import time


def get_deck():
    return {
        "2♥": 2,
        "2♦": 2,
        "2♠": 2,
        "2♣": 2,
        "3♥": 3,
        "3♦": 3,
        "3♠": 3,
        "3♣": 3,
        "4♥": 4,
        "4♦": 4,
        "4♠": 4,
        "4♣": 4,
        "5♥": 5,
        "5♦": 5,
        "5♠": 5,
        "5♣": 5,
        "6♥": 6,
        "6♦": 6,
        "6♠": 6,
        "6♣": 6,
        "7♥": 7,
        "7♦": 7,
        "7♠": 7,
        "7♣": 7,
        "8♥": 8,
        "8♦": 8,
        "8♠": 8,
        "8♣": 8,
        "9♥": 9,
        "9♦": 9,
        "9♠": 9,
        "9♣": 9,
        "T♥": 10,
        "T♦": 10,
        "T♠": 10,
        "T♣": 10,
        "J♥": 10,
        "J♦": 10,
        "J♠": 10,
        "J♣": 10,
        "Q♥": 10,
        "Q♦": 10,
        "Q♠": 10,
        "Q♣": 10,
        "K♥": 10,
        "K♦": 10,
        "K♠": 10,
        "K♣": 10,
        "A♥": 11,
        "A♦": 11,
        "A♠": 11,
        "A♣": 11,
    }


def update_aces(hand):
    while sum(hand.values()) > 21:
        found_an_ace = False
        for card in hand:
            if card[0].startswith("A"):
                hand[card] = 1
        if not found_an_ace:
            break


def print_cards(player, hand):
    time.sleep(0.25)
    print(f"{player}'s cards: ")
    if player == "Dealer" and len(hand) == 2:
        first_card = list(hand)[0]
        print(" ___   ___ ", end=" ")
        print()
        print(f"|{first_card[0]}  | |#  |", end=" ")
        print()

        print(f"| {first_card[1]} | | # |", end=" ")
        print()

        print(f"|__{first_card[0]}| |__#|", end=" ")
        print()
    else:
        for card in hand:
            print(" ___ ", end=" ")

        print()

        for card in hand:
            print(f"|{card[0]}  |", end=" ")

        print()

        for card in hand:
            print(f"| {card[-1]} |", end=" ")

        print()
        for card in hand:
            print(f"|__{card[0]}|", end=" ")

        print(f" ({sum(hand.values())})")
    print()


def add_card(player, hand, deck):
    card = random.choice(list(deck.items()))
    deck.pop(card[0])

    hand[card[0]] = card[1]

    aces = [card for card in hand if card.startswith("A")]

    if len(aces) > 1:
        hand[aces[1]] = 1
    update_aces(hand)
    # print(hand)
    time.sleep(0.5)
    if player == "Dealer" and len(hand) == 2:
        print("Dealer gets a mystery card!")
    else:
        print(f"{player} gets a {card[0]}!")
