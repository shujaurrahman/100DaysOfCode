# Drawing a square using turtle
from turtle import Turtle,Screen
turtle=Turtle()
screen=Screen()

turtle.shape("turtle")
turtle.color("purple")
turtle.shapesize(1,1,2)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)

for _ in range(4):
    turtle.right(90)
    turtle.forward(100)
screen.exitonclick()