import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tummy = Turtle()
tummy.pensize(width=5)
tummy.speed(500)
directions = [0, 90, 180, 270]

tummy.shape('turtle')


# colors = ['gray', 'royal blue', 'medium turquoise', 'medium sea green', 'tan', 'light salmon',
#           'rosy brown', 'dark slate blue', 'lavender']

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


for _ in range(1000):
    tummy.color(random_color())
    tummy.forward(random.randint(1, 30))
    tummy.setheading(random.choice(directions))
