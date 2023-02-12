import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

"""Create the main Screen"""
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('white')
screen.title("Turtle Crossing Game")
screen.tracer(0)

state = True
while state:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()