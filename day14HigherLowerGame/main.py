import random

from game_data import *
from art import *


# Format the account data into printable format.
def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, {description}, from {country}."




score = 0
should_continue = True

def compare(account_a, account_b, guess):
    global score
    global should_continue
    followers_a = account_a['follower_count']
    followers_b = account_b['follower_count']
    if guess == 'a' and followers_a > followers_b:
        score += 1
        print(f"You're right! Current score: {score}")
    elif guess == 'b' and followers_a < followers_b:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = False


# Generate  a random account from the game data
account_b = random.choice(data)
while should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ")
    compare(account_a, account_b, guess)
