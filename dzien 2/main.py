print(f"Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? "))/100
total_tip = bill*tip_percentage
people = int(input("How many people to split the bill? "))
final_amount = round((bill+total_tip)/people, 2)

print(f"Each person should pay: ${final_amount}")