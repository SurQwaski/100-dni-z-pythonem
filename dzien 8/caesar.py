import string
import assets
ALPHABET = list(string.ascii_lowercase)
is_done = False

def caesar(direction, original_text, shift_amount):
    encrypted_message = ""

    if(direction == "decode"):
        shift_amount *= -1

    for letter in original_text:
        if letter not in ALPHABET:
            encrypted_message += letter
        else:
            original_position = ALPHABET.index(letter)

            shifted_position = (original_position + shift_amount) % len(ALPHABET)        
            encrypted_message += ALPHABET[shifted_position]

    print(f"Here is your {choice}d message: {encrypted_message}")

print(assets.logo)

while not is_done:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type shift number:\n"))
    caesar(direction=choice, original_text=text, shift_amount=shift)
    decision = input("Type 'yes' if you want to try again. Otherwise type 'no'.\n").lower()
    if decision == 'no':
        is_done = True
        print("Goodbye ^^")
