from game_data import data
from assets import GAME_LOGO, GAME_LOGO_VS, GAME_MESSAGE
import random

def fetch_subject(game_data):
    """Chooses a random subject from a list of dictionaries.
    Returns a dicitionary with keys name, follower_count, description, country."""
    subject = random.choice(game_data)
    return subject

def fetch_valid_input():
     "Prompts user to input a decision and makes sure the decision is correct."
     correct_data = ["A", "a", "B", "b"]
     done = False
     while not done:
        raw_input = input("Who has more followers? Type 'A' or 'B'. " )
        if raw_input in correct_data:
            return raw_input.lower()
        else:
            print("Incorrect input. Please try again. ")

def collect_valid_subjects():
    """Fetches two subjects and ensures that they aren't the same."""
    subject_a = fetch_subject(data)
    subject_b = fetch_subject(data)

    same_subjects = subject_a["name"] == subject_b["name"]

    while same_subjects:
        subject_b = fetch_subject(data)
        if subject_a["name"] != subject_b["name"]:
            same_subjects = False

    return subject_a, subject_b

def swap_and_prepare_next(subject_a, subject_b):
    "Swaps account A with account B and fetches another for the game to continue."
    subject_a = subject_b
    subject_b = fetch_subject(data)

    same_subjects = subject_a["name"] == subject_b["name"]
    
    while same_subjects:
        subject_b = fetch_subject(data)
        if subject_a["name"] != subject_b["name"]:
            same_subjects = False   
    
    return subject_a, subject_b

def compare_followers(subject_a, subject_b):
    "Calculates a:b ratio of followers. Returns string with word describing the ratio."
    a = subject_a["follower_count"]
    b = subject_b["follower_count"]

    ratio = a/b

    if ratio > 1:
        return "a"
    elif ratio == 1:
        return "equal"
    else:
        return "b"

def match_guess(player_guess, target_answer):
    """Compares player's guess with answer and returns a string with verdict."""
    verdict = ""
    if target_answer == "equal" or player_guess == target_answer:
        verdict = "pass"
    else:
        verdict = "fail"
    return verdict

def higher_or_lower():
    print(GAME_LOGO)
    print(GAME_MESSAGE)

    game_over = False
    account_a, account_b = collect_valid_subjects()
    answer = compare_followers(account_a,account_b)
    score = 0

    while not game_over:
        print(f"Compare A: {account_a['name']}, {account_a['description']}, from {account_a['country']}")
        print(f"With follower count: {account_a['follower_count']}")
        print(GAME_LOGO_VS)
        print(f"Compare B: {account_b['name']}, {account_b['description']}, from {account_b['country']}")

        guess = fetch_valid_input()
        res = match_guess(guess, answer)

        if res == "pass":
            score += 1
            print(f"You pass! Current score: {score}")
            account_a, account_b = swap_and_prepare_next(subject_a=account_a, subject_b=account_b)
            answer = compare_followers(account_a,account_b)
        else:
            game_over = True
            print(f"Sorry that's wrong. Final score: {score}")

should_continue = True           
while should_continue:
    higher_or_lower()
    decision = input("Type 'r' to try again! ").lower()
    if decision != "r":
        should_continue = False