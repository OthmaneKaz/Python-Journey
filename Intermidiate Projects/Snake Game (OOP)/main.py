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

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

state = True

while state:
    screen.update()
    time.sleep(0.1)

    snake.move()


"""Onclick Exit Condition"""
screen.exitonclick()
