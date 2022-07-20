from turtle import Turtle , Screen
import time
from snake_class import Snake
from food_class import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)
screen.listen()

score = Turtle()
snake = Snake()
food = Food()
food_score = 0

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.snake_move()

    if snake.head.distance(food) < 15:
        food.food_refresh()
        food_score += 1
        score.write('Score:', align='center')
screen.exitonclick()
