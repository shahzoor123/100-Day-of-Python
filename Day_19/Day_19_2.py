import turtle
import random
from turtle import Turtle, Screen

turtle.colormode(255)
y_positions = [10, 50, 90, 130, 170, -50]
colors = ['blue', 'red', 'pink', 'green', 'brown', 'yellow']

for num in range(0, 5):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.goto(x=-230, y=y_positions[num])
    tim.color(colors[num])

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
screen.exitonclick()
