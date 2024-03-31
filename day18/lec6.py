import turtle as t 
from turtle import Turtle,Screen
import random



def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t=(r,g,b)

tim=Turtle()
screen=Screen()
direction=[0,90,180,270]

screen.exitonclick()

for steps in range(20):
    tim.color(random_color)
    tim.setheading(random.choice(direction))
    tim.forward(10)
