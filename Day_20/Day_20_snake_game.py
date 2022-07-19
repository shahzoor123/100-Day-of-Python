import random
from turtle import Turtle, Screen
import time

x_positions = [-20, -40, -60]
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)

segments = []
for turtles in range(3):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape('square')
    new_turtle.color('white')
    new_turtle.goto(x_positions[turtles], y=0)
    segments.append(new_turtle)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()
