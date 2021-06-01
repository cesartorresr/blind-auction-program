from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bid_active = True
dictionary = {}
def bidding_record(bidding_track):
  highest_bid = 0
  winner = ""
  for key in bidding_track:
    value = bidding_track[key]
    if value > highest_bid:
      highest_bid = value
      winner = key
  print(f"The winner is {winner} with {highest_bid}")
while bid_active:
  
  name = input("What's your name?: ")
  bid = int(input("What's your bid?$ "))
  dictionary[name] = bid

  Ask_other_users = input("There are others users that want to bid? Type 'Yes' or 'No': ").lower()
  if Ask_other_users == "yes":
    clear()
  else:
    bid_active = False
    bidding_record(dictionary)

