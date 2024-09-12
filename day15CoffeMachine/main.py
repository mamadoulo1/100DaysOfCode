from data import *

profit = 0
is_on = True


def is_resources_sufficient(order_ingredients):
    for key in order_ingredients:
        if order_ingredients[key] >= resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = float(input("How many quarters?"))
    dimes = float(input("How many dimes?"))
    nickles = float(input("How many nickles?"))
    pennies = float(input("How many pennies?"))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return total


def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy!")


while is_on:
    choice = input("“What would you like? (espresso/latte/cappuccino): ")
    if choice.lower() == 'off':
        is_on = False
    elif choice.lower() == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])

