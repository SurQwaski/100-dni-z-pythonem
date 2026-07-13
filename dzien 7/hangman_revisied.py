import random
import assets
import string

ALPHABET = list(string.ascii_lowercase)

chosen_word = random.choice(assets.WORDS)
placeholder = ""
for _ in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
guessed_letters = []
lives = 6


while not game_over:
    print(f"{lives} lives left.")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You have already guessed the letter {guess}")
        continue
    elif guess not in ALPHABET:
        print(f"Invalid character. Use letters only.")
        continue

    guessed_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        print(f"There is no letter '{guess}' in the answer. You lose a life.")
        lives -= 1
    else:
        print(f"You've guessed right!")
    
    print(assets.HANGMAN_PICS[lives])

    if "_" not in display:
        print(f"You win!")
        game_over = True
    elif lives == 0:
        print(f"You ran out of lives. You lose!\nThe answer was: {chosen_word}")
        game_over = True