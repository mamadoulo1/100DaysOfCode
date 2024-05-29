import random

from game_data import *
from art import *


def celebrity():
    choose = random.choice(data)
    return choose


score = 0
should_continue = False


def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


should_continue = False
while not should_continue:
    celebrity1 = celebrity()
    celebrity2 = celebrity()
    if celebrity1 == celebrity2:
        celebrity1 = celebrity()
    print(f"Compare A: {format_data(celebrity1)}.")
    print(vs)
    print(f"Compare B: {format_data(celebrity2)}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_followers = celebrity1['follower_count']
    b_followers = celebrity2['follower_count']
    if check_answer(choice, a_followers, b_followers):
        score += 1
        print(f"You're right! Current score: {score}.")

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue = True
