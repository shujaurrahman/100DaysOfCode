from turtle import Screen
import random
import turtle as t

color_list=[(211, 210, 210), (189, 167, 122), (210, 212, 215), (58, 91, 111), (113, 43, 35), (212, 208, 210), (208, 212, 209), (162, 89, 64), (171, 183, 169), (135, 149, 70), (66, 44, 42), (128, 160, 172), (101, 79, 89), (83, 132, 108), (108, 39, 45), (39, 61, 47), (47, 40, 41), (211, 196, 126), (175, 150, 153), (36, 71, 88), (179, 105, 81), (36, 67, 83), (102, 142, 114), (208, 184, 180), (181, 199, 177), (206, 183, 186), (149, 117, 121), (51, 70, 58), (181, 196, 200), (178, 192, 206)]
t.colormode(255)

tim=t.Turtle()
tim.penup()
tim.hideturtle()
screen=Screen()
tim.speed("fastest")
tim.setheading(230)
tim.forward(300)
tim.setheading(0)

num_0f_dots=100
for dots in range(1,num_0f_dots+1):
    tim.dot(20,color_list[random.randint(0,29)])
    tim.forward(50) 
    if dots%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen.exitonclick()