from turtle import Turtle,Screen
import random
tim=Turtle()
screen=Screen()

tim.shape("turtle")
color=["green yellow	","chocolate","dark magenta","dark green","cyan","dark orange","deep sky blue"]

# angle =360/number_of_sides

def drawShape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for num in range(2,11):
    tim.color(random.choice(color))
    drawShape(num)

screen.exitonclick()