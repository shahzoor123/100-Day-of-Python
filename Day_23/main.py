import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('medium sea green')
screen.listen()
player = Player()
car = CarManager()

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
            game_is_on = False

screen.exitonclick()