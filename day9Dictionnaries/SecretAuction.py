from art import logo
# HINT: You can call clear() to clear the output in the console.
my_dict = {}
print(logo)


def high_bidder(bidding_record):
    high_bidder = 0
    for key in bidding_record:
        bidding_amount = bidding_record[key]
        if bidding_amount > high_bidder:
            high_bidder = bidding_amount
            winner = high_bidder
            return winner


contin = True
while not contin:
    name = input("Enter a name")
    bid = input("Ask a Bid")
    my_dict[name] = bid

user = input("Do you want to continue")
if user == "no":
    contin = True
    high_bidder(my_dict)

elif user == "yes":
    contin = True
