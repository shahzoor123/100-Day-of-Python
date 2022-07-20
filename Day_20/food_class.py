from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('green')
        self.speed('fastest')
        food_x = random.randint(-280, 280)
        food_y = random.randint(-280, 280)
        self.goto(food_x, food_y)
