import random

letters = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPrRsStTwWuUxXyYzZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"
password = []

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

for letter in range(nr_letters):
    letter = random.choice(letters)
    password.append(letter)

for number in range(nr_numbers):
    number = random.choice(numbers)
    password.append(number)

for symbol in range(nr_symbols):
    symbol = random.choice(symbols)
    password.append(symbol)

random.shuffle(password)
password = "".join(password)

print(f"Your password: {password} {len(password)}")
