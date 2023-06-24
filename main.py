from replit import clear
from art import logo

print(logo)

bids = {}

def find_highest_bidder(bidding_record):
  highest_bid = max(bidding_record.values())
  winner = max(bidding_record, key=bidding_record.get)
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while True:
  name = input("What is your name? ")
  price = int(input("What is your bid? "))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if should_continue == "no":
    break
  clear()

find_highest_bidder(bids)
