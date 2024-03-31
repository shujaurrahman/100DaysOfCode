from turtle import Turtle,Screen
import random

tim=Turtle()
screen=Screen()
tim.shape("turtle")
color=["green yellow","chocolate","dark magenta","dark green","cyan","dark orange","deep sky blue"]
direction=[0,90,180,270]
tim.speed("fastest")

for _ in range(100):
    tim.pensize(5)
    tim.color(random.choice(color))
    tim.setheading(random.choice(direction))
    tim.forward(10)

screen.exitonclick()