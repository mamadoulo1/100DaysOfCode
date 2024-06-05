import random
from turtle import *
from random import *
import heroes

########### Challenge 1 - Draw a Square ########

tim = Turtle()
tim.shape("turtle")
tim.color("red")
print(heroes.gen())

# tim.penup()
# tim.forward(100)
# tim.pendown()
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
turtle = Turtle()

# for i in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
directions = [0, 90, 180, 270]


# num_sides = 3
# while num_sides < 11:
#     for _ in range(num_sides):
#         turtle.color(choice(colours))
#         angle = 360 / num_sides
#         turtle.forward(100)
#         turtle.right(angle)
#     num_sides += 1


# for i in range(100):
#     for color in ('red', 'magenta', 'blue',
#                   'cyan', 'green', 'white',
#                   'yellow'):
#         turtle.color(color)
#         turtle.circle(100)
#         turtle.left(10)
#     turtle.hideturtle()


timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.shape("turtle")
timmy.speed("fastest")
angle = [0, 90, 180, 270]


def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    colour = (red, green, blue)
    return colour


def draw_circles(num_of_gap):
    for _ in range(int(360 / num_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.right(num_of_gap)



draw_circles(20)

screen = Screen()
screen.exitonclick()
