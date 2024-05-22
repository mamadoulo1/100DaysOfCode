from logo import *

# Calculator
# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


my_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)
for item in my_dict:
    print(item)
should_continue = False
while not should_continue:
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))
    operations = input("Which operations (+ - * / do you want to do ?: ")
    answer = my_dict[operations](num1, num2)

    print(f"{num1} {operations} {num2} = {answer}")
    contin = input("Type 'y' if you want to continue or 'n' to exit. :")
    if contin == 'y':
        should_continue = False
    else:
        should_continue = True
