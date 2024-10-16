from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_maker = CoffeeMaker()
money_maker = MoneyMachine()
menu = Menu()

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice.lower() == 'off':
        is_on = False
    elif choice.lower() == 'report':
        coffee_maker.report()
        money_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_maker.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


