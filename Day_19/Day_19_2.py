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
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[num])
    new_turtle.color(colors[num])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"Wow the race is wined by {turtle.pencolor()} turtle your bet was on the right horse")
            else:
                print(f"The race is wined by {turtle.pencolor()} turtle your bet was not on the right horse")




screen.exitonclick()