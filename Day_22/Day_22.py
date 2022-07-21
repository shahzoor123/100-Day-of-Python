from turtle import Turtle, Screen
from paddal_class import Paddle
screen = Screen()
screen.title('Pong Game')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
