import game_art
import random

art = [game_art.rock, game_art.paper, game_art.scissors]
choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n"))
print(art[choice - 1])

computer_choice = random.randint(1,3)

print(f"Computer chose: \n" + art[computer_choice - 1])

outcome = (choice - computer_choice) % 3

if not outcome:
    print("Draw")
elif outcome == 1:
    print("You win!")
else:
    print("You lose")
