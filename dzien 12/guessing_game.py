from assets import GUESS_LOGO, WELCOME_MESSAGE_GUESS
import random

def set_difficulty():
    """Prompts the user to set the difficulty of the game.
    Returns amount of lives according to the chosen diffciulty"""

    done = False
    difficulty = input("Choose game difficulty. You can choose 'easy' or 'hard'. ").lower()
    while not done:
        if difficulty == "easy":
            attempts = 10
            done = True
        elif difficulty == "hard":
            attempts = 5
            done = True
        else:
            difficulty = input("Invalid input. Try again. ").lower()
    print(f"You chose {difficulty} difficulty. That means you have {attempts} tries to guess the number.")
    return attempts

def fetch_valid_input():
    """Prompts user to guess a number and validates the guess."""
    UPPER_BOUND = 101
    done = False

    while not done:
            raw_input = (input("Guess a number from 1 to 100. "))
            if not raw_input.isnumeric():
                  print("Input is not a valid number. Please try again. ")
            else:
                  number = int(raw_input)
                  if number not in range(1,UPPER_BOUND):
                       print("Number is not within expected range. Please try again.")
                  else:
                        done = True

    return number

def check_guess(guess,answer):
    """Compares the player's guess with answer.
    Returns a feedback message and True/False if a guess matched the expected answer."""

    is_correct = False
    if guess == answer:
        message = f"You guessed correctly! The secret number was {answer}."
        is_correct = True
    elif guess > answer:
        message = f"Too high! Try again."
    else:
        message = f"Too low! Try again."
    return is_correct, message

def guessing_game():
    game_over = False
    secret_number = random.randint(1,100)

    print(GUESS_LOGO)
    print(WELCOME_MESSAGE_GUESS)
    lives = set_difficulty()

    while not game_over:
        player_guess = fetch_valid_input()
        is_correct, message = check_guess(player_guess,secret_number)

        print(message)

        if is_correct:
            game_over = True
        else:
            lives -= 1
            if lives != 0:
                print(f"{lives} tries remaining.")
            else:
                print(f"You ran out of lives! The correct number was: {secret_number}.")
                game_over = True

guessing_game()