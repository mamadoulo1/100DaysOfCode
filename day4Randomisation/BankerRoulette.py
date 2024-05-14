
# names_string contains the input values provided.
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
names_string = input("Entrez les noms :")
names = names_string.split(", ")
random = random.randint(0, len(names)-1)
print(f"{names[random]} is going to buy the meal today!")

