from data import *

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
profit = 0


def process_coins():
    """Return the total"""
    print("Please insert coins.")
    quarters = int(input("How many quarters ?"))
    dimes = int(input("How many dimes ?"))
    nickles = int(input("How many nickles ?"))
    pennies = int(input("How many pennies ?"))
    total = round((0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies), 2)
    return total


def is_ressources_sufficient(order_ingredients):
    """Check if the ressources are sufficient"""
    global resources
    for key in order_ingredients:
        if order_ingredients[key] >= resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def is_transaction_sucessfull(money_received, drink_cost):
    """Check if transactions was successful"""
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingretients):
    """Make a coffe"""
    for item in order_ingretients:
        resources[item] -= order_ingretients[item]
    print(f"Here is your {drink_name} ☕ Enjoy ?")


should_stop = True
while should_stop:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == 'off':
        should_stop = False
    elif user_input == 'report':
        print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${profit}")
    else:
        drink = MENU[user_input]
        if is_ressources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_sucessfull(payment, drink["cost"]):
                make_coffee(user_input, drink['ingredients'])
