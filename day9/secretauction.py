import art
print(art.logo)
bids={}

bidding_finished=False
def highest_bidder(bids_dictionary):
    for bidder in bids_dictionary:
        highest_bid=0
        bid_amount=bids_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The highest bid is by {winner} and the bid amount is {highest_bid}.")

while not bidding_finished:
    name=input("What is your name? ")
    bid_amount=int(input("What is your bid? $"))
    bids[name]=bid_amount
    should_continue=input("Are there any other bidder ? Type 'Yes' or 'No': ").lower()
    if should_continue=="no":
        bidding_finished=True
        highest_bidder(bids)
    
