import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

tummy = Turtle()
screen = Screen()


def move_forwards():
    tummy.forward(20)


def move_backwards():
    tummy.backward(20)


def clear_screen():
    tummy.clear()


def counter_clockwise():
    tummy.left(20)


def clockwise():
    tummy.left(-20)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.exitonclick()
