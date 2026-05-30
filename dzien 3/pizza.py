print("Welcome to Python Pizza Deliveries!")
size = input("What kind of pizza would you like? S, M or L? ")
pepperoni = input("Would you like some pepperoni with that? (y or n) ")
extra_cheese = input("Would you like some extra cheese? (y or n) ")

if size == "S": 
    bill = 15
elif size == "M": 
    bill = 20
elif size == "L": 
    bill = 25
else: print("Invalid size")

if pepperoni == "y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y": bill += 1

print(f"Your total bill comes to {bill}$.")
