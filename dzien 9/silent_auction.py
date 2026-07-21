import assets

auction_over = False
bids_placed = {}

def find_highest_bidder(bids):
    highest_bid = 0
    winner = None
    for key in bids:
        if bids[key] > highest_bid:
            winner = key
            highest_bid = bids[key]

    if winner:
        print(f"The winner is {winner} with a bid of ${highest_bid}")
    else:
        print("No valid bets were placed.")
            
print(assets.logo)

while not auction_over:
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    bids_placed[name] = bid
    decision = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    if decision == "yes":
        print("\n" * 20)
    elif decision == "no":
        auction_over = True

find_highest_bidder(bids=bids_placed)


