MENU = {
    "espresso" : {
        "ingredients":{
            "water" : 50,
            "coffee" : 18
        }
        , "cost" : 1.5,
        },
    "latte" : {
        "ingredients":{
            "water" : 200,
            "milk" : 150,
            "coffee" : 18,
        }
        , "cost" : 2.5,
        },
    "cappuccino" : {
        "ingredients":{
            "water" : 250,
            "milk" : 100,
            "coffee" : 18
        }
        , "cost" : 3.0,
        }
}

RESOURCES = {
    "water" : [100,"ml"],
    "milk" : [300,"ml"],
    "coffee" : [200,"g"],
    "money" : [1,"$"]
}

def print_report():
    for ingredient in RESOURCES:
        print(f"{ingredient} : {''.join(map(str,RESOURCES[ingredient]))}")

def fetch_input():
    raw_input = ""
    valid_input = ["espresso","latte","cappuccino","off","report"]
    while raw_input not in valid_input:
        raw_input = input("What would you like? (espresso/latte/cappuccino) ")
    return raw_input

def fetch_recipe_ingredients(drink):
    current_recipe = MENU[drink]["ingredients"]
    return current_recipe

def compare_resources(drink):
    recipe = fetch_recipe_ingredients(drink)
    is_enough = True
    for ingredient in recipe:
        if recipe[ingredient] > RESOURCES[ingredient][0]:
            print(f"Sorry there is not enough {ingredient}")
            is_enough = False
            break
    return is_enough

def process_coins():
    quarters = ""
    dimes = ""
    nickles = ""
    pennies = ""
    done = False
    print("Please insert coins.")

    while not done:
        quarters = input("How many quarters? ")
        dimes = input("How many dimes? ")
        nickles = input("How many nickles? ")
        pennies = input("How many pennies? ")
        valid = quarters.isnumeric() and dimes.isnumeric() and nickles.isnumeric() and pennies.isnumeric()
        if valid:
            done = True
    total = 0.25 * int(quarters) + 0.1 * int(dimes) + 0.05 * int(nickles) + 0.01 * int(pennies)

    return total

def assess_transaction(total, drink):
    price = MENU[drink]["cost"]
    is_enough = True
    change = 0
    
    if total < price:
        is_enough = False
        return is_enough, change
    else:
        change = total - price
        return is_enough, change

def conduct_transaction(drink):
    total = process_coins()
    is_enough, change = assess_transaction(total,drink)

    if not is_enough:
        print("Sorry, that's not enough money. Money refunded. ")
        return False
    else:
        if change > 0:
            total -= change
            print(f"Here is {round(change,2)}$ change.")
            return total
        else:
            return total

def update_supply(recipe,total):
    for ingredient in recipe:
        RESOURCES[ingredient][0] -= recipe[ingredient]
    RESOURCES["money"][0] += total

def prepare_coffee(drink):
    enough_resources = compare_resources(drink)
    if enough_resources:
        transaction_result = conduct_transaction(drink)
        if transaction_result:
            recipe = fetch_recipe_ingredients(drink)
            update_supply(recipe, transaction_result)
            print(f"Here is your {drink}. Enjoy!")
    else:
        return False



turned_on = True

while turned_on:
    decision = fetch_input()
    if decision == "off":
        turned_on = False
    elif decision == "report":
        print_report()
    else:
        prepare_coffee(decision)
