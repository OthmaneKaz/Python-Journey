"""Imports"""
from turtle import Screen
from snake import Snake
import time

"""Create the main Screen"""
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

state = True

while state:
    screen.update()
    time.sleep(0.1)

"""Onclick Exit Condition"""
screen.exitonclick()
