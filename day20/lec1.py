# snake game using python turtle 

# we will be build this in 2 day 20 and 21
# day20 3 steps

# Build the snake using 3 squares
# move the snake
# control the snake 

from turtle import Turtle,Screen
import random,time

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)


squares=[0,-20,-40]
segments=[]
for square in range(0,3):
    new_Square=Turtle("square")
    new_Square.color("white")
    new_Square.penup()
    new_Square.goto(x=squares[square],y=0)
    segments.append(new_Square)



is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(10)

    for seg_num in range(len(segments)-1,0,-1):
        new_x=segments[seg_num-1].xcor()
        new_y=segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)

screen.exitonclick()
