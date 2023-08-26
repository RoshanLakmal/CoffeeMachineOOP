from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def user_commands(user_input):
    coffee_menu = Menu()
    coffee_maker = CoffeeMaker()

    if user_input == "off":
        exit()
    elif user_input == "report":
        coffee_maker.report()
    else:
        drink = coffee_menu.find_drink(user_input)

def start_coffee_machine():
    coffee_menu = Menu()
    user_command = input(f"What would you like? ({coffee_menu.get_items()}): ")
    user_commands(user_command)
    start_coffee_machine()


start_coffee_machine()