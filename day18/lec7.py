
from turtle import Screen,Turtle
import random

def random_color():
    hex_chars = '0123456789ABCDEF'
    color_code = '#'
    for _ in range(6):
        color_code += random.choice(hex_chars)
    return color_code




tim=Turtle()
tim.shape("turtle")
direction=[0,90,180,270]
radius=[5,10,15,20,30]
tim.speed("fastest")

def draw_spiral(gap):     
    for steps in range(int(360/gap)):
        tim.pensize(1)
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+gap)

draw_spiral(5)

screen=Screen()
screen.exitonclick()