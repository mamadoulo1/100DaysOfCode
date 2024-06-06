from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clockwise():
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(45)


def clockwise():
    tim.circle(-100)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=counter_clockwise)
screen.onkey(key="D", fun=clockwise)
screen.onkey(key="C", fun=clear)
screen.exitonclick()
