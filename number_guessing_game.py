###
# A simple number guessing game
#
import random

# Randomly chosen number to be guessed from 1 to 100
number_to_guess = random.randint(1, 100)
user_guess = 0

print("Guess the number between 1 and 100!")

while user_guess != number_to_guess:
    user_guess = int(input("Enter your guess: "))

    if user_guess < 1:
        print("Too low! Try again.")
    elif user_guess >100:
        print("Too high! Try again.")
    elif user_guess == number_to_guess:
        print("Congratulations! You guessed the correct number.")
    else:
        print(f"Too bad! You guessed the wrong number. The computer's guess was {number_to_guess}.")