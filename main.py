from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def user_commands(user_input):


    if user_input == "off":
        exit()
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = coffee_menu.find_drink(user_input)

        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

def start_coffee_machine():
    user_command = input(f"What would you like? ({coffee_menu.get_items()}): ")
    user_commands(user_command)
    start_coffee_machine()


start_coffee_machine()