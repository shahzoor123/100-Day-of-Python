from turtle import Turtle, Screen
import random

tummy = Turtle()
tummy.pensize(width=5)
tummy.speed(500)
directions = [0, ]

tummy.shape('turtle')
# colors = ['gray', 'royal blue', 'medium turquoise', 'medium sea green', 'tan', 'light salmon',
#           'rosy brown', 'dark slate blue', 'lavender']

colors = ['gray', 'black']

for _ in range(1000):
    tummy.color(random.choice(colors))
    tummy.forward(random.randint(1, 40))
    tummy.right(random.randint(1, 200))


