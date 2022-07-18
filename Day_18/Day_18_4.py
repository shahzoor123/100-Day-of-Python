import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

tummy = Turtle()
tummy.speed(100)

tummy.shape('turtle')
rgb = [(26, 108, 164), (194, 38, 81), (237, 161, 50), (234, 215, 86), (223, 137, 176), (143, 108, 57)]
tummy.penup()
tummy.setheading(255)
tummy.forward(300)
tummy.setheading(0)
number_of_dots = 101

for dot_counts in range(1, number_of_dots):
    tummy.penup()
    tummy.forward(50)
    tummy.dot(20, random.choice(rgb))
    tummy.penup()
    if dot_counts % 10 == 0:
        tummy.setheading(90)
        tummy.forward(50)
        tummy.setheading(180)
        tummy.forward(500)
        tummy.setheading(0)






screen = Screen()
screen.exitonclick()
