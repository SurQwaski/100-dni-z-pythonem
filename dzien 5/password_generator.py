import random

letters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPrRsStTwWuUxXyYzZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"
temp_dictionary = []
password = ""

nr_letters = int(input("How many letters would you like in your password?\n")) + 1
nr_numbers = int(input("How many numbers would you like in your password?\n")) + 1
nr_symbols = int(input("How many symbols would you like in your password?\n")) + 1



for letter in range(1,nr_letters):
    letter = random.choice(letters)
    temp_dictionary.append(letter)

for number in range(1,nr_numbers):
    number = random.choice(numbers)
    temp_dictionary.append(number)

for symbol in range(1,nr_symbols):
    symbol = random.choice(symbols)
    temp_dictionary.append(symbol)

for character in range(1,len(temp_dictionary)+1):
    rng_index = random.randint(0,len(temp_dictionary) - 1)
    password += temp_dictionary.pop(rng_index)

print(f"Your password: {password}")
