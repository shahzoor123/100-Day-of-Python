import turtle
import random
from turtle import Turtle, Screen

is_race_on = False
turtle.colormode(255)
y_positions = [10, 50, 90, 130, 170, -50]
colors = ['blue', 'red', 'pink', 'green', 'brown', 'yellow']
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
all_turtles = []


for num in range(0, 5):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.goto(x=-230, y=y_positions[num])
    tim.color(colors[num])


if user_bet:
    is_race_on = True

while is_race_on:
    random_distance = random.randint(0, 10)
    turtle.forward(random_distance)


screen.exitonclick()