#!/usr/bin/env python3
"""
Number Guessing Game
A fun game where the player tries to guess a randomly generated number
"""

import random

def number_guessing_game():
    """Main game function"""
    print("=" * 50)
    print("NUMBER GUESSING GAME")
    print("=" * 50)
    print("\nWelcome! I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100!")
                attempts -= 1  # Don't count invalid attempts
                continue

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\n🎉 Congratulations! You guessed it!")
                print(f"The number was {secret_number}")
                print(f"You won in {attempts} attempts!")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            attempts -= 1  # Don't count invalid attempts

    else:
        print(f"\n💔 Game Over! You've used all {max_attempts} attempts.")
        print(f"The secret number was: {secret_number}")

    # Ask to play again
    play_again = input("\nWould you like to play again? (yes/no): ")
    if play_again.lower() in ['yes', 'y']:
        number_guessing_game()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    number_guessing_game()
