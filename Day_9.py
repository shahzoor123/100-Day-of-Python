import os
import mod.bidding_art as art
print(art.logo)
bid = {}
def find_highest_bidding(bidding_record):
    higest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > higest_bid:
            higest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with the bid of ${higest_bid}')    

should_continue = True
while should_continue:
    print("Welcome to the bidding silent programe")
    name = input("what is your name?: ")
    price = int(input("what is your bid?: $ "))
    user = input("is there any other user who wants to bid if there is type 'yes' if not than type 'no'\n")
    bid[name] = price
    if user == "no":
        should_continue = False
        find_highest_bidding(bid)
    else:
        os.system("cls")
        continue    

