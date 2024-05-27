# Number Guessing Game Objectives:
import random
from art import *

# Include an ASCII art logo.
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# Allow the player to submit a guess for a number between 1 and 100.
result = random.randint(1, 100)

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
attempts = 0
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    global attempts
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5


should_continue = False
def check_answer(guess, result):
    # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
    global should_continue
    if guess == result:
        # If they got the answer correct, show the actual answer to the player.
        print(f"You got it! The answer was {result}.")
        should_continue = True
    elif guess > result:
        print("Too high.\nGuess again.")
    else:
        print("Too low.\nGuess again.")

set_difficulty()
while not should_continue:
    # Track the number of turns remaining.
    print(f"You have {attempts} remaining to guess the number.")
    attempts -= 1
    guess = int(input("Make a guess: "))
    check_answer(guess, result)

    # If they run out of turns, provide feedback to the player.
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        should_continue = True







