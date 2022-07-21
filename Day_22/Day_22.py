from turtle import Turtle, Screen

screen = Screen()
screen.title('Pong Game')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

paddle1 = Turtle()
paddle1.shape('square')
paddle1.color('white')
paddle1.penup()
paddle1.turtlesize(5, 1)
paddle1.goto(350, 0)


def up():
    new_y = paddle1.ycor() + 40
    paddle1.goto(paddle1.xcor(), new_y)


def down():
    new_y = paddle1.ycor() - 40
    paddle1.goto(paddle1.xcor(), new_y)


screen.listen()
screen.onkey(up, 'Up')
screen.onkey(down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
