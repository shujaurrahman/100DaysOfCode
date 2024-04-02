from turtle import Turtle,Screen
import random,time
from snake import Snake 
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)

new_snake=Snake()
screen.listen()
screen.onkey(new_snake.Up,"Up")
screen.onkey(new_snake.down,"Down")
screen.onkey(new_snake.left,"Left")
screen.onkey(new_snake.right,"Right")

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move()
screen.exitonclick()
