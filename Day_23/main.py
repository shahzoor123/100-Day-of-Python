import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('medium sea green')
screen.listen()
player = Player()
car = CarManager()
level = ScoreBoard()

screen.onkey(player.up, 'Up')
screen.onkey(player.down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    for every_car in car.all_car:
        if player.distance(every_car) < 20:
            level.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        car.increase_speed()
        level.level_up()

screen.exitonclick()
