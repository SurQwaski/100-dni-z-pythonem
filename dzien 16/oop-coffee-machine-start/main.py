from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

main_menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

on = True

while on:
    correct_drink = None
    while correct_drink is None:
        order = input(f"What would you like? ({main_menu.get_items()}) ")
        if order == "report":
            coffe_maker.report()
            money_machine.report()
        elif order == "off":
            on = False
            break
        else:
            correct_drink = main_menu.find_drink(order)

    if not on:
        break

    can_make = coffe_maker.is_resource_sufficient(drink=correct_drink)
    if can_make:
        transcaction_complete = money_machine.make_payment(cost=correct_drink.cost)
        if transcaction_complete:
            coffe_maker.make_coffee(order=correct_drink)