print(
    '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\'''
)

new_bidder = True
blind_auction = {}
while new_bidder:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    blind_auction[name] = bid
    new_bidder = input("Is there another bidder? (y/n): ") == "y"
    print("\n" * 100)

max_key = max(blind_auction, key=blind_auction.get)
print(
    f"The person who bid the most is {max_key} with a bid of {blind_auction[max_key]}$"
)
