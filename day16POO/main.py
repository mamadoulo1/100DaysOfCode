from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino/): ”
coffee_maker = CoffeeMaker()
money_maker = MoneyMachine()
menu = Menu()
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/):")
    options = menu.get_items()
    # TODO 2: Turn off the Coffee Machine by entering “ off ” to the prompt.
    if choice == "off":
        is_on = False
    # TODO 3: Print report
    elif choice == "report":
        coffee_report = coffee_maker.report()
        money_report = money_maker.report()
        print(coffee_report)
        print(money_report)
    else:
        drink = menu.find_drink(choice)
        # TODO 4: Check resources sufficient, Process coins And Check transaction successful?.
        if coffee_maker.is_resource_sufficient(drink) and money_maker.make_payment(drink.cost):
            # TODO 5: Make Coffee
            coffee_maker.make_coffee(drink)

