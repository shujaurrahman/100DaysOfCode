from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def move_forwared():
    tim.forward(20)

def  move_backward():
    tim.backward(20)

def counter_clock():
    n=tim.heading()+10
    tim.setheading(n)

def clockwise():
    n=tim.heading()-10
    tim.setheading(n)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w",fun=move_forwared)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=counter_clock)
screen.onkey(key="d",fun=clockwise)

screen.onkey(key="c",fun=clear)

screen.exitonclick()