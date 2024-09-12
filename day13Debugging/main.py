from random import randint

dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 5)
print(dice_images[dice_num])


def my_function():
    for i in range(1, 20):
        if i == 10:
            print("You got it !")


my_function()

try:
    age = int(input("How old are you?  "))
except ValueError:
    print("Invalid number. Please try again with a valid number: ")
    age = int(input("How old are you?"))