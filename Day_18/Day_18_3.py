import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tummy = Turtle()
tummy.speed(1500)
directions = [0, 90, 180, 270]

tummy.shape('turtle')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


for _ in range(100):
    for _ in range(255):
        tummy.color(random_color())
        tummy.circle(100)
        tummy.left(10)


