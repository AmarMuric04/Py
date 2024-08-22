from logo import logo

print(logo)


def find_highest_bidder(bidders):
    winner = ""
    highest_bid = 0
    for bidders_key in bidders:
        bid_amount = bidders[bidders_key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidders_key
    print(f"The person who bid the most is {winner} with a bid of {highest_bid}$")


new_bidder = True
blind_auction = {}
while new_bidder:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    blind_auction[name] = bid
    new_bidder = input("Is there another bidder? (y/n): ").lower() == "y"
    print("\n" * 100)

find_highest_bidder(blind_auction)
# max_key = max(blind_auction, key=blind_auction.get)
# print(
#     f"The person who bid the most is {max_key} with a bid of {blind_auction[max_key]}$"
# )
