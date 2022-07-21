from turtle import Turtle, Screen
from paddal_class import Paddle
from ball_class import Ball
import time
from scoreboard_class import ScoreBoard

screen = Screen()
screen.title('Pong Game')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_movement()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 100 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()


screen.exitonclick()
