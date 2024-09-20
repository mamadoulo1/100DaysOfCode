from turtle import Turtle, Screen

tim = Turtle()
turtle = Turtle()

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)

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