from replit import clear
from art import *
#HINT: You can call clear() to clear the output in the console.

print(logo)
keep_bidding = True
auction_bids = {}

while keep_bidding:
  name = input("What is your name?\n")
  bid = int(input("How much do you want to bid? \n$"))
  
  auction_bids[name] = bid

  new_bids = input("Are there any others who want to bid? Type 'yes' to continue or 'no' to end. \n").lower()
  if new_bids == 'yes':
    clear()
  else:
    keep_bidding = False

winning_person = max(auction_bids, key=auction_bids.get) #gets the key with the max int from auction_bids dictionary
highest_bid = max(auction_bids.values()) #gets the value with the max int from auction_bids dictionary

print(f"\nThe winner is {winning_person} with a bid of ${highest_bid}")
