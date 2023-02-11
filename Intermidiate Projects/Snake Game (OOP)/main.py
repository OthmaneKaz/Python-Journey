"""Imports"""
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

"""Create the main Screen"""
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

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

    """detect collision with food"""
    if snake.head.distance(food) < 17.5:
        food.refresh()
        scoreboard.increase_score()

    """detect collision with wall"""
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        state = False
        scoreboard.gameover()

"""Onclick Exit Condition"""
screen.exitonclick()
